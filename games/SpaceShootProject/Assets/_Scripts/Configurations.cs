using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
public class Configurations : MonoBehaviour {

	AudioSource menuClick;
	public AudioClip[] sounds;
	AudioSource[] sources;
	public static int enemy0Score = 100, enemy1Score = 100, enemy2Score = 100, enemy3Score = 100, enemy4Score = 100, 
		bgSongChoice=3, winSongChoice=1, weaponSound = 0;

	public static float volumeVal = 1;

	float scroll0, scroll1, scroll2, scroll3, scroll4;

	public Text text0,text1,text2,text3,text4;

	public Material mat0,mat1,mat2,mat3,mat4,bgmat;

	public Dropdown bgSongChoices, winSongChoices, weaponSounds, color0, 
		color1, color2, color3, color4, imageChoices;

	public Image preview;

	public Slider volumebar;

	Sprite x,y,z;
	int imageChoice = 0;

	void Awake()
	{
		sounds = Resources.LoadAll<AudioClip> ("sound");
		x = Resources.Load<Sprite> ("Space 1");
		y = Resources.Load<Sprite>("galaxy 1");
		z = Resources.Load<Sprite> ("blackhole 1");
	}

	// Use this for initialization
	void Start () {
		
		sources = GetComponents<AudioSource> ();

		color0.onValueChanged.AddListener (delegate {
			color0Change ();
		});

		color1.onValueChanged.AddListener (delegate {
			color1Change ();
		});

		color2.onValueChanged.AddListener (delegate {
			color2Change ();
		});

		color3.onValueChanged.AddListener (delegate {
			color3Change ();
		});

		color4.onValueChanged.AddListener (delegate {
			color4Change ();
		});

		bgSongChoices.onValueChanged.AddListener (delegate {
			bgSongChange ();

		});
	
		winSongChoices.onValueChanged.AddListener (delegate {
			winSongChange ();

		});

		weaponSounds.onValueChanged.AddListener (delegate {
			weaponSoundChange ();

		});

		imageChoices.onValueChanged.AddListener (delegate {
			pictureUIChange ();
		});

	}
	
	// Update is called once per frame
	void Update () {
		scroll0 = GameObject.Find ("Enemy 0 Slider").GetComponent<Slider>().value;
		scroll1 = GameObject.Find ("Enemy 1 Slider").GetComponent<Slider>().value;
		scroll2 = GameObject.Find ("Enemy 2 Slider").GetComponent<Slider>().value;
		scroll3 = GameObject.Find ("Enemy 3 Slider").GetComponent<Slider>().value;
		scroll4 = GameObject.Find ("Enemy 4 Slider").GetComponent<Slider>().value;

		enemy0Score = Mathf.FloorToInt(scroll0 * 100);
		enemy1Score = Mathf.FloorToInt(scroll1 * 100);
		enemy2Score = Mathf.FloorToInt(scroll2 * 100);
		enemy3Score = Mathf.FloorToInt(scroll3 * 100);
		enemy4Score = Mathf.FloorToInt(scroll4 * 100);

		text0.text = ""+enemy0Score;
		text1.text = ""+enemy1Score;
		text2.text = ""+enemy2Score;
		text3.text = ""+enemy3Score;
		text4.text = ""+enemy4Score;

		volumeVal = volumebar.value;
		AudioListener.volume = volumebar.value;
	}

	void OnGUI()
	{
		if (GUI.Button (new Rect (Screen.width/2 - 150, Screen.height - 95, 300, 35), "EXIT MENU")) {
			
			sources[0].Play ();
			StartCoroutine("back"); //Sends player back to second screen
		}

		if (GUI.Button (new Rect (Screen.width/2 - 130, Screen.height - 240, 260, 35), "CONFIRM BACKGROUND CHANGE")) {
			sources[0].Play ();
			if (imageChoice == 0) {
				bgmat.SetTexture("_MainTex",Resources.Load<Texture>("Space_Transparent"));
			}
			else if (imageChoice == 1) {
				bgmat.SetTexture("_MainTex",Resources.Load<Texture>("galaxy"));
			}
			else if (imageChoice == 2) {
				bgmat.SetTexture("_MainTex",Resources.Load<Texture>("blackhole"));
			}
		}
	}

	IEnumerator back()
	{
		yield return new WaitForSeconds(.5f);
		SceneManager.LoadScene ("SecondScreen");
	}

	void bgSongChange()
	{
		if (bgSongChoices.value == 0) {
			bgSongChoice = 3;
			sources [1].Stop ();
			sources [1].clip = sounds [3];
			sources [1].Play ();
		} else if (bgSongChoices.value == 1) {
			bgSongChoice = 6;
			sources [1].Stop ();
			sources [1].clip = sounds [6];
			sources [1].Play ();
		} else {
			bgSongChoice = 0;
			sources [1].Stop ();
			sources [1].clip = sounds [0];
			sources [1].Play ();
		}
	}

	void winSongChange()
	{
		if (winSongChoices.value == 0) {
			winSongChoice = 3;
		} else {
			winSongChoice = 4;
		} 
	}

	void weaponSoundChange()
	{
		if (weaponSounds.value == 0) {
			weaponSound = 0;
			sources [2].clip = sounds [4];
			sources [2].Play ();
		} else {
			weaponSound = 1;
			sources [2].clip = sounds [2];
			sources [2].Play ();
		} 
	}

	void color0Change()
	{
		if (color0.value == 0) {
			mat0.SetColor ("_Color", Color.white);
		} else if (color0.value == 1) {
			mat0.SetColor ("_Color", Color.green);
		} else if (color0.value == 2) {
			mat0.SetColor ("_Color", Color.blue);
		} else if (color0.value == 3) {
			mat0.SetColor ("_Color", Color.red);
		}
	}
	void color1Change ()
	{
		if (color1.value == 0) {
			mat1.SetColor ("_Color", Color.white);
		} else if (color1.value == 1) {
			mat1.SetColor ("_Color", Color.green);
		} else if (color1.value == 2) {
			mat1.SetColor ("_Color", Color.blue);
		} else if (color1.value == 3) {
			mat1.SetColor ("_Color", Color.red);
		}
	}
	void color2Change ()
	{
		if (color2.value == 0) {
			mat2.SetColor ("_Color", Color.white);
		} else if (color2.value == 1) {
			mat2.SetColor ("_Color", Color.green);
		} else if (color2.value == 2) {
			mat2.SetColor ("_Color", Color.blue);
		} else if (color2.value == 3) {
			mat2.SetColor ("_Color", Color.red);
		}
	}
	void color3Change ()
	{
		if (color3.value == 0) {
			mat3.SetColor ("_Color", Color.white);
		} else if (color3.value == 1) {
			mat3.SetColor ("_Color", Color.green);
		} else if (color3.value == 2) {
			mat3.SetColor ("_Color", Color.blue);
		} else if (color3.value == 3) {
			mat3.SetColor ("_Color", Color.red);
		}
	}
	void color4Change ()
	{
		if (color4.value == 0) {
			mat4.SetColor ("_Color", Color.white);
		} else if (color4.value == 1) {
			mat4.SetColor ("_Color", Color.green);
		} else if (color4.value == 2) {
			mat4.SetColor ("_Color", Color.blue);
		} else if (color4.value == 3) {
			mat4.SetColor ("_Color", Color.red);
		}
	}

	void pictureUIChange()
	{
		if (imageChoices.value == 0) {
			imageChoice = 0;
			preview.overrideSprite =  x;
		} else if (imageChoices.value == 1) {
			imageChoice = 1;
			preview.overrideSprite = y;
		} else {
			imageChoice = 2;
			preview.overrideSprite = z;
		}
	}
}
