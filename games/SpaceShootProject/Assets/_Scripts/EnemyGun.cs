using UnityEngine;
using System.Collections;

public class EnemyGun : MonoBehaviour {

	public GameObject EnemyBullet;

	// Use this for initialization
	void Start () {
		Invoke ("FireEnemyBullet", 1f);
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	void FireEnemyBullet()
	{
		GameObject playerShip = GameObject.Find ("Hero");

		if (playerShip != null) {
			GameObject bullet = (GameObject)Instantiate (EnemyBullet);

			bullet.transform.position = transform.position;

			Vector2 direction = playerShip.transform.position - bullet.transform.position;
			bullet.GetComponent<ProjectileEnemy> ().SetDirection (direction);
		}
	}
}
