using UnityEngine;
using System.Collections;

public class GameOver : MonoBehaviour {

	GUIStyle label = new GUIStyle(); //Style for the label that declares who won

	// Use this for initialization
	void Start () {
		label.fontSize = 70; 
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKeyDown ("space")) {
			Application.LoadLevel("MainMenu"); //Loads the Main Menu when the space bar is pressed
		}
		if (Input.GetKeyDown ("r")) {
			Application.LoadLevel("MainGame"); //Plays the Main Game when the R key is pressed
		}
	}

	void OnGUI()
	{ //Determines if player won or lost based on the the static variables in the Main script
		if (Main.wins > Main.loss) {
			GUI.Label(new Rect(Screen.width/2-150,Screen.height/2-100,400,30), "YOU WIN!",label);
		} else if (Main.loss > Main.wins) {
			GUI.Label(new Rect(Screen.width/2-150,Screen.height/2-100,400,30), "YOU LOSE!",label);
		} else {
			GUI.Label(new Rect(Screen.width/2-150,Screen.height/2-100,400,30), "IT'S A DRAW!",label);
		}
	}
}
