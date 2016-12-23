using UnityEngine;

public class hpManager : MonoBehaviour
{
	//public PlayerHealth playerHealth;       // Reference to the player's heatlh.
	public GameObject healthPack;                // The enemy prefab to be spawned.
	public float spawnTime = 10f;            // How long between each spawn.
	public Transform[] spawnPoints; 		// An array of the spawn points this enemy can spawn from.
	public static int hpSpawned;
	
	void Start ()
	{
		// Call the Spawn function after a delay of the spawnTime and then continue to call after the same amount of time.
		InvokeRepeating ("Spawn", spawnTime, spawnTime);
	}
	
	
	void Spawn ()
	{
		
		// Find a random index between zero and one less than the number of spawn points.
		int spawnPointIndex = Random.Range (0, spawnPoints.Length);
		
		
		if (hpSpawned < 4) {
			// Create an instance of the enemy prefab at the randomly selected spawn point's position and rotation.
			Instantiate (healthPack, spawnPoints [spawnPointIndex].position, spawnPoints [spawnPointIndex].rotation);
			hpSpawned++;
		}
	} 
	
	public static void decreaseHpOnMap(int i){
		hpSpawned -= i;
	}
	public static void resetHpOnMap() {
		hpSpawned = 0;
	}
}