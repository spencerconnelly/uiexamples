using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Main : MonoBehaviour {


	bool bronze, silver, gold, paused;
	AudioSource[] sources;
	AudioClip[] sounds;
	public Text scoreText,counter0,counter1,counter2,counter3,counter4;
	static public int score = 0, enemy0count=0,enemy1count=0,enemy2count=0,
		enemy3count=0,enemy4count=0;


	static public Main S;
	static public Dictionary<WeaponType, WeaponDefinition> W_DEFS;
	public GameObject[] prefabEnemies;
	public float enemySpawnPerSecond = 0.5f; // # Enemies/second
	public float enemySpawnPadding = 1.5f; // Padding for position
	public WeaponDefinition[] weaponDefinitions;
	public WeaponType[] activeWeaponTypes;
	public bool ________________;
	public GameObject prefabPowerUp;
	public WeaponType[] powerUpFrequency = new WeaponType[] {
		WeaponType.Blaster, WeaponType.Blaster,
		WeaponType.Spread,
		WeaponType.Shield };
	public float enemySpawnRate; // Delay between Enemy spawns
	void Awake() {
		paused = false;
		bronze = false;
		silver = false;
		gold = false;

		sounds = Resources.LoadAll<AudioClip> ("sound");
		sources = (AudioSource[]) GetComponents<AudioSource> ();
		AudioListener.volume = Configurations.volumeVal;
		sources [1].clip = sounds [Configurations.bgSongChoice];
		sources [1].Play ();
		S = this;
		// Set Utils.camBounds
		Utils.SetCameraBounds(GetComponent<Camera>());
		// 0.5 enemies/second = enemySpawnRate of 2
		enemySpawnRate = 1f/enemySpawnPerSecond; // 1
		// Invoke call SpawnEnemy() once after a 2 second delay
		Invoke( "SpawnEnemy", enemySpawnRate ); // 2
		// A generic Dictionary with WeaponType as the key
		W_DEFS = new Dictionary<WeaponType, WeaponDefinition>();
		foreach( WeaponDefinition def in weaponDefinitions ) {
			W_DEFS[def.type] = def;
		}
	}
	static public WeaponDefinition GetWeaponDefinition( WeaponType wt ) {
		// Check to make sure that the key exists in the Dictionary
		// Attempting to retrieve a key that didn't exist, would throw an error,
		// so the following if statement is important.
		if (W_DEFS.ContainsKey(wt)) {
			return( W_DEFS[wt]);
		}
		// This will return a definition for WeaponType.none,
		// which means it has failed to find the WeaponDefinition
		return( new WeaponDefinition() );
	}
	void Start() {
		bronze = false;
		silver = false;
		gold = false;
		score = 0;
		enemy0count = 0;
		enemy1count = 0;
		enemy2count = 0;
		enemy3count = 0;
		enemy4count = 0;
		Utils.SetCameraBounds(GetComponent<Camera>());
		activeWeaponTypes = new WeaponType[weaponDefinitions.Length];
		for ( int i=0; i<weaponDefinitions.Length; i++ ) {
			activeWeaponTypes[i] = weaponDefinitions[i].type;
		}
	}
	public void SpawnEnemy() {
		// Pick a random Enemy prefab to instantiate
		int ndx = Random.Range(0, prefabEnemies.Length);
		GameObject go = Instantiate( prefabEnemies[ ndx ] ) as GameObject;
		// Position the Enemy above the screen with a random x position
		Vector3 pos = Vector3.zero;
		float xMin = Utils.camBounds.min.x+enemySpawnPadding;
		float xMax = Utils.camBounds.max.x-enemySpawnPadding;
		pos.x = Random.Range( xMin, xMax );
		pos.y = Utils.camBounds.max.y + enemySpawnPadding;
		go.transform.position = pos;
		// Call SpawnEnemy() again in a couple of seconds
		Invoke( "SpawnEnemy", enemySpawnRate ); // 3
	}
	public void DelayedRestart( float delay ) {
		// Invoke the Restart() method in delay seconds
		Invoke("Restart", delay);
	}
	public void Restart() {
		// Reload _Scene_0 to restart the game
		SceneManager.LoadScene ("_Scene_0");
	}
	public void ShipDestroyed( Enemy e ) {
		// Potentially generate a PowerUp
		if (Random.value <= e.powerUpDropChance) {
			// Random.value generates a value between 0 & 1 (though never == 1)
			// If the e.powerUpDropChance is 0.50f, a PowerUp will be generated
			// 50% of the time. For testing, it's now set to 1f.
			// Choose which PowerUp to pick
			// Pick one from the possibilities in powerUpFrequency
			int ndx = Random.Range(0,powerUpFrequency.Length);
			WeaponType puType = powerUpFrequency[ndx];
			// Spawn a PowerUp
			GameObject go = Instantiate( prefabPowerUp ) as GameObject;
			PowerUP pu = go.GetComponent<PowerUP>();
			// Set it to the proper WeaponType
			pu.SetType( puType );
			// Set it to the position of the destroyed ship
			pu.transform.position = e.transform.position;
		}
	}

	void OnGUI()
	{
		if (GUI.Button (new Rect (Screen.width/2 - 150, Screen.height - 55, 300, 35), "PAUSE")) {
			sources [0].Play ();
			if (paused == false) {
				Time.timeScale = 0;
				paused = true;
			} else {
				Time.timeScale = 1;
				paused = false;
			}
		}
		if (GUI.Button (new Rect (200, Screen.height - 55, 300, 35), "RESTART")) {
			sources [0].Play ();
			StartCoroutine ("restart");
		}
		if (GUI.Button (new Rect (Screen.width/2 + 225, Screen.height - 55, 300, 35), "EXIT GAME")) {
			sources [0].Play ();
			StartCoroutine ("exit");
		}
	}

	IEnumerator restart()
	{
		yield return new WaitForSeconds(.5f);
		SceneManager.LoadScene ("_Scene_0");
	}

	IEnumerator exit()
	{
		yield return new WaitForSeconds(.5f);
		SceneManager.LoadScene ("StartingScreen");
	}

	void Update()
	{
		scoreText.text = "Score:  "+score;
		counter0.text = "enemy0: " + enemy0count;
		counter1.text = "enemy1: " + enemy1count;
		counter2.text = "enemy2: " + enemy2count;
		counter3.text = "enemy3: " + enemy3count;
		counter4.text = "enemy4: " + enemy4count;
		if (score <= GameLevels.bPtLevelUp)
			bronzeLevel ();
		if (score > GameLevels.bPtLevelUp && score <= GameLevels.sPtLevelUp)
			silverLevel ();
		if (score < GameLevels.gPtLevelUp && score > GameLevels.sPtLevelUp)
			goldLevel ();
		if (score > GameLevels.gPtLevelUp)
			SceneManager.LoadScene ("WinningScreen");
	}

	void bronzeLevel()
	{
		if(bronze == false){
			if (GameLevels.bDifficulty == 0)
				enemySpawnPerSecond = .2f;
			else if (GameLevels.bDifficulty == 1)
				enemySpawnPerSecond = .3f;
			else if (GameLevels.bDifficulty == 2)
				enemySpawnPerSecond = .4f;
			else if (GameLevels.bDifficulty == 3)
				enemySpawnPerSecond = .6f;
			else if (GameLevels.bDifficulty == 4)
				enemySpawnPerSecond = .9f;
			enemySpawnRate = 1f/enemySpawnPerSecond; // 1
			// Invoke call SpawnEnemy() once after a 2 second delay
			Invoke( "SpawnEnemy", enemySpawnRate ); // 2
			bronze = true;
		}
	}

	void silverLevel()
	{
		if (silver == false) {
			if (GameLevels.bDifficulty == 0)
				enemySpawnPerSecond = .4f;
			else if (GameLevels.bDifficulty == 1)
				enemySpawnPerSecond = .5f;
			else if (GameLevels.bDifficulty == 2)
				enemySpawnPerSecond = .6f;
			else if (GameLevels.bDifficulty == 3)
				enemySpawnPerSecond = .7f;
			else if (GameLevels.bDifficulty == 4) 
				enemySpawnPerSecond = .9f;
			enemySpawnRate = 1f / enemySpawnPerSecond; // 1
			// Invoke call SpawnEnemy() once after a 2 second delay
			Invoke ("SpawnEnemy", enemySpawnRate); // 2
			silver = true;
		}
	}

	void goldLevel()
	{
		if(gold == false){
			if (GameLevels.bDifficulty == 0)
				enemySpawnPerSecond = .6f;
			else if (GameLevels.bDifficulty == 1)
				enemySpawnPerSecond = .8f;
			else if(GameLevels.bDifficulty == 2)
				enemySpawnPerSecond = .9f;
			else if(GameLevels.bDifficulty == 3)
				enemySpawnPerSecond = 1f;
			else if(GameLevels.bDifficulty == 4)
				enemySpawnPerSecond = 1.7f;
			enemySpawnRate = 1f/enemySpawnPerSecond; // 1
			// Invoke call SpawnEnemy() once after a 2 second delay
			Invoke( "SpawnEnemy", enemySpawnRate ); // 2
			gold = true;
		}
	}
}
