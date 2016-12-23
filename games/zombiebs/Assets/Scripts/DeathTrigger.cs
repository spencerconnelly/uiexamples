using UnityEngine;
using System.Collections;

public class DeathTrigger : MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

    void onTriggerEnter2D (Collider2D other) {

	
		Application.LoadLevel (Application.loadedLevel);
		}



}
