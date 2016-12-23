import { Component, OnInit } from '@angular/core';
import {Auth} from '../auth.service';
@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css'],
  providers: [Auth]
})
export class ProfileComponent implements OnInit {
  email:string;
  constructor(private auth: Auth) { 
    //i want to be able to show email and show all the articles that have been saved to their account but i cannot figure it out
  }

  ngOnInit() {
    
  }

}
