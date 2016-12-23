using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;
public class Hero : MonoBehaviour {
	[SerializeField] private float _shieldLevel = 1;
	static public Hero S; // Singleton
	// These fields control the movement of the ship
	public float speed = 30;
	public float rollMult = -50;
	public float pitchMult = 30;
	// Ship status information
	public bool ____________________________;
	public Bounds bounds;
	// Declare a new delegate type WeaponFireDelegate
	public delegate void WeaponFireDelegate();
	// Create a WeaponFireDelegate field named fireDelegate.
	public WeaponFireDelegate fireDelegate;
	public float gameRestartDelay = 2f;
	public Weapon[] weapons;
	AudioSource weaponSound;
	AudioClip[] sounds = new AudioClip[2];

	void Awake() {
		sounds [0] = Resources.Load<AudioClip> ("sound/laser");
		sounds [1] = Resources.Load<AudioClip> ("sound/gun");
		weaponSound = GetComponent<AudioSource> ();
		weaponSound.clip = sounds [Configurations.weaponSound];
		S = this; // Set the Singleton
		bounds = Utils.CombineBoundsOfChildren (this.gameObject);
	}

	void Start(){
		// Reset the weapons to start _Hero with 1 blaster
		ClearWeapons();
		weapons[0].SetType(WeaponType.Blaster);
		bounds = Utils.CombineBoundsOfChildren (this.gameObject);
	}

	void Update () {
		// Pull in information from the Input class
		float xAxis = Input.GetAxis("Horizontal"); // 1
		float yAxis = Input.GetAxis("Vertical"); // 1
		// Change transform.position based on the axes
		Vector3 pos = transform.position;
		pos.x += xAxis * speed * Time.deltaTime;
		pos.y += yAxis * speed * Time.deltaTime;
		transform.position = pos;
		bounds.center = transform.position;
		// Use the fireDelegate to fire Weapons
		// First, make sure the Axis("Jump") button is pressed
		// Then ensure that fireDelegate isn't null to avoid an error
		if (Input.GetAxis ("Jump") == 1 && fireDelegate != null) { // 1
			weaponSound.Play();
			fireDelegate ();

		} 

		Vector3 off = Utils.ScreenBoundsCheck(bounds, BoundsTest.onScreen); // 2
		if ( off != Vector3.zero ) { // 3
			pos -= off;
			transform.position = pos;
		}
		// Rotate the ship to make it feel more dynamic // 2
		transform.rotation = Quaternion.Euler(yAxis*pitchMult,xAxis*rollMult,0);
	}

	public GameObject lastTriggerGo = null;

	void OnTriggerEnter(Collider other) {
		// Find the tag of other.gameObject or its parent GameObjects
		GameObject go = Utils.FindTaggedParent(other.gameObject);
		// If there is a parent with a tag
		if (go != null) {
			if (go == lastTriggerGo) {
				return;
			}
			lastTriggerGo = go; 
			if (go.tag == "Enemy") {
				shieldLevel--;
				// Destroy the enemy
				Destroy(go); 

			}else if (go.tag == "PowerUp") {
				// If the shield was triggerd by a PowerUp
				AbsorbPowerUp(go);
			} else {
				print("Triggered: "+go.name); 
			}
		} else {
			// Otherwise announce the original other.gameObject
			print("Triggered: "+other.gameObject.name); 
		}
	}

	public float shieldLevel {
		get {
			return( _shieldLevel ); // 1
		}
		set {
			_shieldLevel = Mathf.Min( value, 4 ); // 2
			// If the shield is going to be set to less than zero
			if (value < 0) { // 3
				Destroy(this.gameObject);

				Main.S.DelayedRestart(gameRestartDelay);
			}
		}
	}
	public void AbsorbPowerUp( GameObject go ) {
		PowerUP pu = go.GetComponent<PowerUP>();
		switch (pu.type) {
		case WeaponType.Shield: // If it's the shield
			shieldLevel++;
			break;
		default: // If it's any Weapon PowerUp
			// Check the current weapon type
			if (pu.type == weapons[0].type) {
				// then increase the number of weapons of this type
				Weapon w = GetEmptyWeaponSlot(); // Find an available weapon
				if (w != null) {
					// Set it to pu.type
					w.SetType(pu.type);
				}
			} else {
				// If this is a different weapon
				ClearWeapons();
				weapons[0].SetType(pu.type);
			}
			break;
		}
		pu.AbsorbedBy( this.gameObject );
	}
	Weapon GetEmptyWeaponSlot() {
		for (int i=0; i<weapons.Length; i++) {
			if ( weapons[i].type == WeaponType.none ) {
				return( weapons[i] );
			}
		}
		return( null );
	}
	void ClearWeapons() {
		foreach (Weapon w in weapons) {
			w.SetType(WeaponType.none);
		}
	}
}
