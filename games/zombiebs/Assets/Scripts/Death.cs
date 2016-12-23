using UnityEngine;
using System.Collections;
[RequireComponent (typeof (AudioSource))]
public class Death : MonoBehaviour {
	
	public static AudioSource sorry;
	// Use this for initialization
	void Start () {
		sorry = gameObject.GetComponent<AudioSource> ();
	}
	
	// Update is called once per frame
	public static void playSong () {
		sorry.Play ();
	}
}
