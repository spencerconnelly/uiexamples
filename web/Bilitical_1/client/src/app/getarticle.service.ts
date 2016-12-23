import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable }     from 'rxjs/Observable';
@Injectable()
export class GetarticleService {

  constructor(private http: Http) { }
  
  angular: any;

  public getProgArticles(){
    return null;
  }

  public getConservArticles(){
    return this.http.get('/myapi/conservative')
        .map(this.extractData)
        .catch(this.handleError);
  }

  public getLiberalArticles(){
    return null;
  }

  private extractData(res: Response){
    let body = res.json();
    return body.data || { };
  }

  private handleError(error: Response | any){
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
    } else {
      errMsg = error.message ? error.message : error.toString();
   }
    console.error(errMsg);
    return Observable.throw(errMsg);
   }
}
