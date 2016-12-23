using UnityEngine;
using System.Collections;

[RequireComponent (typeof (Controller2D))]
public class Player : MonoBehaviour {

	public Animator anim;
	public Material my_material;
	public bool facingRight = true;
	public float jumpHeight = 6;
	public float timeToJumpApex = 1f;
	float accelerationTimeAirborne = .2f;
	float accelerationTimeGrounded = .1f;
	float moveSpeed = 6;
	public static int jumpcounter = 0;
	int jumptimes = 2;
	float gravity;
	public static float jumpVelocity;
	public static Vector3 velocity;
	public static float velocityXSmoothing;



	Controller2D controller;
	
	void Start() {
		controller = GetComponent<Controller2D> ();
		anim = GetComponent<Animator> ();
		gravity = -(jumpHeight*2) / Mathf.Pow (timeToJumpApex, 2);
		jumpVelocity = Mathf.Abs(gravity) * timeToJumpApex;
		print ("Gravity: " + gravity + "  Jump Velocity: " + jumpVelocity);
	}
	
	void Update() {

		float h = Input.GetAxis("Horizontal");

		//FLIPPING WHILE MOVING
		if (h > 0 && !facingRight)
			Flip();
		else if (h < 0 && facingRight)
			Flip();


		Vector2 input = new Vector2 (Input.GetAxisRaw ("Horizontal"), Input.GetAxisRaw ("Vertical"));

		//JUMPING
		if (Input.GetKeyDown (KeyCode.W)) {
			jumpcounter++;
			if(jumpcounter<2)
				Jump ();
		}
		if (controller.collisions.below) {
			jumpcounter = 0;
		}

		if (Input.GetKeyDown (KeyCode.Space)) {
			anim.Play("Swing",-1,0f);
			print ("pressed!!!");
		} 

		//MOVING
		if (Input.GetKey (KeyCode.D) || Input.GetKey (KeyCode.A)) {
			anim.Play ("Moving");

		} 
		if (Input.GetKey (KeyCode.Escape)) {
			Application.LoadLevel("StartScreen");
		}
		float targetVelocityX = input.x * moveSpeed;
		velocity.x = Mathf.SmoothDamp (velocity.x, targetVelocityX, ref velocityXSmoothing, (controller.collisions.below) ? accelerationTimeGrounded : accelerationTimeAirborne);
		velocity.y += gravity * Time.deltaTime;

		if (velocity.y < -9.81)
			velocity.y = -9.81f;

		controller.Move (velocity * Time.deltaTime);
	}

	public static void Jump()
	{
		velocity.y = jumpVelocity;
	}

	void Flip()
	{
		facingRight = !facingRight;
		Vector3 theScale = transform.localScale;
		theScale.x *= -1;
		transform.localScale = theScale;
	}
}






