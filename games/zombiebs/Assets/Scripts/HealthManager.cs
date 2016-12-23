using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class HealthManager : MonoBehaviour {
	public static int health;        // The player's health.

	public Text healthText;

	// Use this for initialization
	void Start () {
		health = 100;
		healthText = GameObject.Find ("Healthtext").GetComponent<Text> ();
	
	}

	// Update is called once per frame
	void Update () {
		healthText.text = "Health: " + health;

		if (health > 70)
			healthText.color = Color.green;
		else if (health > 40)
			healthText.color = Color.yellow;
		else
			healthText.color = Color.red;
		if (health <= 0) {
			Destroy (this.gameObject);
			Application.LoadLevel("GameOverScreen");
		}
	
	}

	void OnTriggerEnter2D(Collider2D other)
	{
	
		if (other.name == "zombieImageObject(Clone)") {
			decreaseHealth(10);
			if (HealthManager.health > 100 )
				HealthManager.health = 100;
			
		}


	}

	public static void decreaseHealth(int amount) {

		health -= amount;
	}

}
