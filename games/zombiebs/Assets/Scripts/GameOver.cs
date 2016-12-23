using UnityEngine;
using System.Collections;

public class GameOver : MonoBehaviour {

	// Use this for initialization
	void OnGUI()
	{
		if (GUI.Button (new Rect (Screen.width / 8, Screen.height * 3 / 4, 300, 100), "Play Again")) {
			Application.LoadLevel ("jbiebs");
			//EnemyManager1.decreaseEnemies (100);
			EnemyManager1.resetEnemies();
			hpManager.resetHpOnMap();
		}
		if (GUI.Button (new Rect (Screen.width*6/9,Screen.height*3/4,300,100), "Exit")) 
				Application.Quit();
			
	}
}
