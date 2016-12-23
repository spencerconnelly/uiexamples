using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;
public class SecondScreen : MonoBehaviour {

	AudioSource[] sources;
	AudioClip[] sounds;

	// Use this for initialization
	void Start () {
		sounds = Resources.LoadAll<AudioClip> ("sound");
		sources = (AudioSource[]) GetComponents<AudioSource> ();
		AudioListener.volume = Configurations.volumeVal;
		sources [1].clip = sounds [Configurations.bgSongChoice];
		sources [1].Play ();
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	void OnGUI()
	{
		if (GUI.Button (new Rect (Screen.width/2 + 50, Screen.height/2 - 50, 300, 35), "BEGIN")) {
			sources [0].Play ();
			StartCoroutine ("play"); //Starts the game
		}
		if (GUI.Button (new Rect (Screen.width/2 + 50, Screen.height/2 + 10, 300, 35), "GAME LEVELS")) {
			sources [0].Play ();
			StartCoroutine ("levels");
		}
		if (GUI.Button (new Rect (Screen.width/2 + 50, Screen.height/2 + 70, 300, 35), "CONFIGURATION")) {
			sources [0].Play ();
			StartCoroutine ("config"); //Loads the main game screen
		}
		if (GUI.Button (new Rect (Screen.width/2 + 50, Screen.height/2 + 130, 300, 35), "HISTORY")) {
			sources [0].Play ();
		}
	}

	IEnumerator play()
	{
		yield return new WaitForSeconds(.5f);
		SceneManager.LoadScene ("_Scene_0");
	}

	IEnumerator config()
	{
		yield return new WaitForSeconds(.5f);
		SceneManager.LoadScene ("ConfigurationScene");
	}

	IEnumerator levels()
	{
		yield return new WaitForSeconds(.5f);
		SceneManager.LoadScene ("GameLevelsScreen");
	}
}
