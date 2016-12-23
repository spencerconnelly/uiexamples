using UnityEngine;
using System.Collections;

public class WinningHero : MonoBehaviour {
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
		transform.Rotate(0f,0f,6f*10f*Time.deltaTime);
	}
}
