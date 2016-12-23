using UnityEngine;
using System.Collections;

public class MainMenu : MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	void OnGUI()
	{ //Puts a Start button on the main menu screen
		if (GUI.Button (new Rect (Screen.width/2 - 150, Screen.height - 55, 300, 35), "Begin")) {
			Application.LoadLevel("MainGame"); //Loads the main game screen
		}
	}
}
