import { Injectable } from '@angular/core';
import { tokenNotExpired } from 'angular2-jwt';

let Auth0Lock = require('auth0-lock').default;

var options = {
    auth: {
      redirectURL: 'http://localhost:4200/login'
    }
  };

@Injectable()
export class Auth {

  lock = new Auth0Lock('53qGxyUZtKF41uQDmXF1hsXGDy2wRcpr', 'sconnel6.auth0.com', options);

  userProfile: any;

  constructor() {
    // Set userProfile attribute of already saved profile
    this.userProfile = JSON.parse(localStorage.getItem('profile'));

    // Add callback for the Lock `authenticated` event
    this.lock.on("authenticated", (authResult) => {
      localStorage.setItem('id_token', authResult.idToken);

      // Fetch profile information
      this.lock.getProfile(authResult.idToken, (error, profile) => {
        if (error) {
          // Handle error
          alert(error);
          return;
        }

        localStorage.setItem('profile', JSON.stringify(profile));
        this.userProfile = profile;
      });
    });
  };


   public login() {
     this.lock.show();
   };

   public authenticated() {
     return tokenNotExpired();
   };

   public logout(){
    localStorage.removeItem('id_token');
   };

   public isAdmin(){
      if(this.userProfile.app_metadata.admin == "true"){
        return true;
      } else {
        return false;
      }

      
    }
}
