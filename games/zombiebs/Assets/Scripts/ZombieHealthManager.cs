using UnityEngine;
using System.Collections;

public class ZombieHealthManager : MonoBehaviour {

	ParticleSystem explode;

	public static int health;
	void Start () {
		health = 100;
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	void OnTriggerEnter2D(Collider2D other)
	{
		if (other.gameObject.name == "Feet" ) {

			Player.Jump();
			health -= 49;
		}
		if (other.gameObject.name == "sword") {
			health-= 100;
		}
		if (health <= 0) {
			this.gameObject.GetComponent<EnemyCharacterController1>().nullify();
			explode = this.gameObject.GetComponentInChildren<ParticleSystem>();
			explode.Play ();
			ScoreManager.increase();
			EnemyManager1.decreaseEnemies(1);

			Destroy(this.gameObject,0.5f);


		}
	}
	
}