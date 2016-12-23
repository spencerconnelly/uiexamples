using UnityEngine;

public class EnemyManager1 : MonoBehaviour
{
	//public PlayerHealth playerHealth;       // Reference to the player's heatlh.
	public GameObject enemy;                // The enemy prefab to be spawned.
	public float spawnTime = 3f;            // How long between each spawn.
	public Transform[] spawnPoints; 		// An array of the spawn points this enemy can spawn from.
	public static int enemiesSpawned;

	void Start ()
	{
		// Call the Spawn function after a delay of the spawnTime and then continue to call after the same amount of time.
		InvokeRepeating ("Spawn", spawnTime, spawnTime);
	}
	
	
	void Spawn ()
	{

		// Find a random index between zero and one less than the number of spawn points.
		int spawnPointIndex = Random.Range (0, spawnPoints.Length);


		if (enemiesSpawned < 100) {
			// Create an instance of the enemy prefab at the randomly selected spawn point's position and rotation.
			Instantiate (enemy, spawnPoints [spawnPointIndex].position, spawnPoints [spawnPointIndex].rotation);
			enemiesSpawned++;
		}
	} 

	public static void decreaseEnemies(int i){
		enemiesSpawned -= i;
	}
	public static void resetEnemies(){
		enemiesSpawned = 0;
	}
}