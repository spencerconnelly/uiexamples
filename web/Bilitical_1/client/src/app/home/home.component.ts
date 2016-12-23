import { Component, OnInit } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http'
import {HomearticleComponent} from '../homearticle/homearticle.component';
import { Injectable,Inject } from '@angular/core';
import {Auth} from '../auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [HomearticleComponent],
  providers: [Auth]
})
export class HomeComponent implements OnInit {

  
  centerList:any[];
  libList:any[];
  progList:any[];
  articletitles:any[];

  title1:string;
  title2:string;
  title3:string;
  title4:string;
  title5:string;
  title6:string;
  title7:string;
  title8:string;
  title9:string;
  title10:string;
  title11:string;
  title12:string;
  title13:string;
  title14:string;
  title15:string;
  title16:string;
  title17:string;
  title18:string;
  title19:string;
  title20:string;

  url1:string;
  url2:string;
  url3:string;
  url4:string;
  url5:string;
  url6:string;
  url7:string;
  url8:string;
  url9:string;
  url10:string;
  url11:string;
  url12:string;
  url13:string;
  url14:string;
  url15:string;
  url16:string;
  url17:string;
  url18:string;
  url19:string;
  url20:string;

  dateadd1:string;
  dateadd2:string;
  dateadd3:string;
  dateadd4:string;
  dateadd5:string;
  dateadd6:string;
  dateadd7:string;
  dateadd8:string;
  dateadd9:string;
  dateadd10:string;
  dateadd11:string;
  dateadd12:string;
  dateadd13:string;
  dateadd14:string;
  dateadd15:string;
  dateadd16:string;
  dateadd17:string;
  dateadd18:string;
  dateadd19:string;
  dateadd20:string;
  
  datewrite1:string;
  datewrite2:string;
  datewrite3:string;
  datewrite4:string;
  datewrite5:string;
  datewrite6:string;
  datewrite7:string;
  datewrite8:string;
  datewrite9:string;
  datewrite10:string;
  datewrite11:string;
  datewrite12:string;
  datewrite13:string;
  datewrite14:string;
  datewrite15:string;
  datewrite16:string;
  datewrite17:string;
  datewrite18:string;
  datewrite19:string;
  datewrite20:string;

  

  constructor(@Inject(Http) private http: Http,private auth: Auth) {}


  ngOnInit() {
    this.http.get('/myapi/progressive').map(res => res.json()).subscribe(res => {
      this.title1 = res[res.length - 1].title;
      this.title2 = res[res.length - 2].title;
      this.title3 = res[res.length - 3].title;
      this.title4 = res[res.length - 4].title;
      this.title5 = res[res.length - 5].title;

      console.log(res[0].articleURL);
      this.url1 = res[res.length - 1].articleURL;
      this.url2 = res[res.length - 2].articleURL;
      this.url3 = res[res.length - 3].articleURL;
      this.url4 = res[res.length - 4].articleURL;
      this.url5 = res[res.length - 5].articleURL;

      this.dateadd1 = res[res.length - 1].dateAdded;
      this.dateadd2 = res[res.length - 2].dateAdded;
      this.dateadd3 = res[res.length - 3].dateAdded;
      this.dateadd4 = res[res.length - 4].dateAdded;
      this.dateadd5 = res[res.length - 5].dateAdded;

      this.datewrite1 = res[res.length - 1].dateWritten;
      this.datewrite2 = res[res.length - 2].dateWritten;
      this.datewrite3 = res[res.length - 3].dateWritten;
      this.datewrite4 = res[res.length - 4].dateWritten;
      this.datewrite5 = res[res.length - 5].dateWritten;
    }, err => console.error(err));

    this.http.get('/myapi/liberal').map(res => res.json()).subscribe(res => {
      this.title6 = res[res.length - 1].title;
      this.title7 = res[res.length - 2].title;
      this.title8 = res[res.length - 3].title;
      this.title9 = res[res.length - 4].title;
      this.title10 = res[res.length - 5].title;

      this.url6 = res[res.length - 1].articleURL;
      this.url7 = res[res.length - 2].articleURL;
      this.url8 = res[res.length - 3].articleURL;
      this.url9 = res[res.length - 4].articleURL;
      this.url10 = res[res.length - 5].articleURL;

      this.dateadd6 = res[res.length - 1].dateAdded;
      this.dateadd7 = res[res.length - 2].dateAdded;
      this.dateadd8 = res[res.length - 3].dateAdded;
      this.dateadd9 = res[res.length - 4].dateAdded;
      this.dateadd10 = res[res.length - 5].dateAdded;

      this.datewrite6 = res[res.length - 1].dateWritten;
      this.datewrite7 = res[res.length - 2].dateWritten;
      this.datewrite8 = res[res.length - 3].dateWritten;
      this.datewrite9 = res[res.length - 4].dateWritten;
      this.datewrite10 = res[res.length - 5].dateWritten;
    }, err => console.error(err));

    this.http.get('/myapi/center').map(res => res.json()).subscribe(res => {
      this.title11 = res[res.length - 1].title;
      this.title12 = res[res.length - 2].title;
      this.title13 = res[res.length - 3].title;
      this.title14 = res[res.length - 4].title;
      this.title15 = res[res.length - 5].title;

      this.url11 = res[res.length - 1].articleURL;
      this.url12 = res[res.length - 2].articleURL;
      this.url13 = res[res.length - 3].articleURL;
      this.url14 = res[res.length - 4].articleURL;
      this.url15 = res[res.length - 5].articleURL;

      this.dateadd11 = res[res.length - 1].dateAdded;
      this.dateadd12 = res[res.length - 2].dateAdded;
      this.dateadd13 = res[res.length - 3].dateAdded;
      this.dateadd14 = res[res.length - 4].dateAdded;
      this.dateadd15 = res[res.length - 5].dateAdded;

      this.datewrite11 = res[res.length - 1].dateWritten;
      this.datewrite12 = res[res.length - 2].dateWritten;
      this.datewrite13 = res[res.length - 3].dateWritten;
      this.datewrite14 = res[res.length - 4].dateWritten;
      this.datewrite15 = res[res.length - 5].dateWritten;
    }, err => console.error(err));

    this.http.get('/myapi/conservative').map(res => res.json()).subscribe(res => {
      this.title16 = res[res.length - 1].title;
      this.title17 = res[res.length - 2].title;
      this.title18 = res[res.length - 3].title;
      this.title19 = res[res.length - 4].title;
      this.title20 = res[res.length - 5].title;

      this.url16 = res[res.length - 1].articleURL;
      this.url17 = res[res.length - 2].articleURL;
      this.url18 = res[res.length - 3].articleURL;
      this.url19 = res[res.length - 4].articleURL;
      this.url20 = res[res.length - 5].articleURL;

      this.dateadd16 = res[res.length - 1].dateAdded;
      this.dateadd17 = res[res.length - 2].dateAdded;
      this.dateadd18 = res[res.length - 3].dateAdded;
      this.dateadd19 = res[res.length - 4].dateAdded;
      this.dateadd20 = res[res.length - 5].dateAdded;

      this.datewrite16 = res[res.length - 1].dateWritten;
      this.datewrite17 = res[res.length - 2].dateWritten;
      this.datewrite18 = res[res.length - 3].dateWritten;
      this.datewrite19 = res[res.length - 4].dateWritten;
      this.datewrite20 = res[res.length - 5].dateWritten;
    }, err => console.error(err));


  }
  

  
 


}
