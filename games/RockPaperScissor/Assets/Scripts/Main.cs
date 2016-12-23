using UnityEngine;
using System.Collections;

public class Main : MonoBehaviour {
	//This script is attached to the main camera to run the main game
	public GameObject rockPre, paperPre, scissorPre, pos1, pos2; //prefabs of the objects, pos1 and 2 are the positions of the prefabs
	int compPick; //The choices are represented and compared with numbers 0 = rock, 1 = paper, 2 = scissors
	public static int gamesPlayed, wins, loss, draw; //these are static so the GameOver script can access
	GameObject[] objects = new GameObject[2]; //an array that contains the two pictures of the objects
	GUIStyle label = new GUIStyle(); //style of the GUI labels used


	// Use this for initialization
	void Start () {
		label.normal.textColor = Color.black; //sets the GUIStyle of the label
		label.fontSize = 20;
		gamesPlayed = 0;
		wins = 0;
		loss = 0;
		draw = 0;

	}
	
	// Update is called once per frame
	void Update () {
		objects = GameObject.FindGameObjectsWithTag ("Choice"); //Fills the objects array by finding tagged objects so they can be easily deleted
		if (gamesPlayed == 10) { //checks if gamesPlayed is 10 and then loads the GameOver Screen once this is reached
			Application.LoadLevel("GameOver");
		}
	}

	void OnGUI()
	{
		//Score Labels
		GUI.Label(new Rect(Screen.width/2-40,30,400,30), "Games Played: " + gamesPlayed,label);
		GUI.Label(new Rect(Screen.width/2 - 100, 50, 200, 35), "Wins: " + wins,label);
		GUI.Label(new Rect(Screen.width/2 - 25, 50, 200, 35), "| Losses: " + loss,label);
		GUI.Label(new Rect(Screen.width/2 + 75, 50, 200, 35), "| Draws: " + draw,label);

		//Player Labels
		GUI.Label (new Rect (Screen.width / 4 - 20, Screen.height / 4 - 40, 200, 35), "You:",label);
		GUI.Label (new Rect (3*(Screen.width / 4), Screen.height / 4 - 40, 200, 35), "Computer:",label);

		//Buttons for Choices
		//Rock button is picked
		if (GUI.Button (new Rect (Screen.width/2 - 130, Screen.height - 125, 300, 35), "Rock")) { 
			foreach(GameObject go in objects) //for-loop that deletes the previous objects for the choices
				Destroy(go);
			Instantiate(rockPre,pos1.transform.position,rockPre.transform.rotation); //instantiates the prefab choices at pos1


			computerPick(); //computer picks 

			gamesPlayed++; //adds to gamesPlayed as identified in project flow chart

			if(compPick == 0){ //both players picked rock
				draw++;
			}
			else if(compPick == 1){ //computer picked paper
				loss++;
			}
			else{ //computer picked scissors
				wins++;
			}
		}
		//Paper button is picked
		if (GUI.Button (new Rect (Screen.width/2 - 130, Screen.height - 90, 300, 35), "Paper")) { 
			foreach(GameObject go in objects)
				Destroy(go);
			Instantiate(paperPre,pos1.transform.position,rockPre.transform.rotation);

			computerPick();
			gamesPlayed++;

			if(compPick == 0){ //computer picked rock
				wins++;
			}
			else if(compPick == 1){ //computer picked paper
				draw++;
			}
			else{ //computer picked scissors
				loss++;
			}
		}
		//Scissor button is picked
		if (GUI.Button (new Rect (Screen.width/2 - 130, Screen.height - 55, 300, 35), "Scissors")) {
			foreach(GameObject go in objects)
				Destroy(go);
			Instantiate(scissorPre,pos1.transform.position,rockPre.transform.rotation);

			computerPick();

			gamesPlayed++;

			if(compPick == 0){ //computer picked rock
				loss++;
			}
			else if(compPick == 1){ //computer picked paper
				wins++;
			}
			else{ //computer picked scissors
				draw++;
			}
		}

	}

	//How the computer picks choice
	void computerPick()
	{
		//Random Number Generator that can be 0,1, or 2
		compPick = Random.Range (0, 3);
		if (compPick == 0) {
			Instantiate(rockPre,pos2.transform.position,rockPre.transform.rotation); //Instatiates a rock at pos2
		} 
		else if (compPick == 1) {
			Instantiate(paperPre,pos2.transform.position,paperPre.transform.rotation); //Instatiates paper at pos2
		} 
		else {
			Instantiate(scissorPre,pos2.transform.position,scissorPre.transform.rotation); //Instatiates scissors at pos2
		}
	}
}
