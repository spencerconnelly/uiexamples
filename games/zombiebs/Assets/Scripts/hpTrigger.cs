using UnityEngine;
using System.Collections;

public class hpTrigger : MonoBehaviour {

	void Start () {

	}
	
	// Update is called once per frame
	void Update () {
		
	}

	void OnTriggerEnter2D(Collider2D other)
	{

		if (other.gameObject.tag == "Player") {

			HealthManager.decreaseHealth(-20);
			Destroy(gameObject);
			hpManager.decreaseHpOnMap(1);
		}
	}
}



