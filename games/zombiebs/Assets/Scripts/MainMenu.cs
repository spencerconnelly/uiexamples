using UnityEngine;
using System.Collections;

public class MainMenu : MonoBehaviour {

	// Use this for initialization
	void OnGUI()
	{
		if (GUI.Button (new Rect (Screen.width*1/8,Screen.height*3/4,600,100), "Begin")) {
			Application.LoadLevel("jbiebs");
		}

	}
	
	// Update is called once per frame
	void Update () {

	}
}
