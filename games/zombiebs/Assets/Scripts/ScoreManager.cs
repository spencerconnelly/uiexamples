using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class ScoreManager : MonoBehaviour
{
	public static int score;        // The player's score.

	
	public Text scoreText;        // Reference to the Text component.

	
	void Start ()
	{
		score = 0;
		// Set up the reference.
		scoreText = GameObject.Find ("Text").GetComponent<Text> ();

		// Reset the score.

	}
	
	
	void Update ()
	{
		// Set the displayed text to be the word "Score" followed by the score value.
		scoreText.text = "Score: " + score;
	}

	public static void increase() {
		score = score + 1;
	}

}