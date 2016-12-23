import { Component, OnInit } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';

@Component({
  selector: 'app-articleform',
  templateUrl: './articleform.component.html',
  styleUrls: ['./articleform.component.css']
})
export class ArticleformComponent implements OnInit {

  constructor(private http: Http) { }

  ngOnInit() {
  }

  public submitAddition(title, arturl, datewrite, dateadd, view, flag){
    

    if(flag == "yes"){
      flag = true;
    } else { 
      flag = false;
    }
    let body = JSON.stringify({title: title, articleURL: arturl, viewpoint: view, dateAdded: dateadd, dateWritten: datewrite, flagged: flag});
  
    var headers = new Headers();
    headers.append('Content-Type', 'application/json');
    let options = new RequestOptions({headers: headers});

    console.log(body);

    this.http.post('/myapi/',body,options).map(res => res.json()).subscribe( data => {console.log(data)}, err => console.error(err));
    
  }

}
