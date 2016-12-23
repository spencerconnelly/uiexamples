using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;
public class StartScreen : MonoBehaviour {

	AudioSource[] sources;
	AudioClip[] sounds;
	// Use this for initialization
	void Start () {
		sounds = Resources.LoadAll<AudioClip> ("sound");
		sources = (AudioSource[]) GetComponents<AudioSource> ();
		AudioListener.volume = Configurations.volumeVal;
		sources [1].clip = sounds [Configurations.bgSongChoice];
		sources [1].Play ();
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	void OnGUI()
	{
		if (GUI.Button (new Rect (Screen.width/2 - 150, Screen.height - 95, 300, 35), "NEXT PAGE")) {
			sources [0].Play ();
			StartCoroutine ("next");
		}
		if (GUI.Button (new Rect (Screen.width/2 - 150, Screen.height - 55, 300, 35), "EXIT GAME")) {
			Application.Quit (); //quits the application
		}
	}

	IEnumerator next()
	{
		yield return new WaitForSeconds(.5f);
		SceneManager.LoadScene ("SecondScreen");
	}
}
