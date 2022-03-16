import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Subject } from 'rxjs/internal/Subject';

@Injectable({
  providedIn: 'root'
})

export class LoginAuthService {

  apiURL = 'http://localhost:3000/signupUsers';
  tokenresp: any;

  constructor(
    private http: HttpClient,
    private route: Router,
  ) { }

  private _updatemenu = new Subject<void>();
  get updatemenu() {
    return this._updatemenu;
  }

  proceedLogin(usercred: any) {
    return this.http.post(this.apiURL, usercred);
  }

  GenerateRefreshToken() {
    let input = {
      "jwtToken": this.GetToken(),
      "refreshToken": this.GetRefreshToken()
    }
    return this.http.post(this.apiURL + 'refresh', input);
  }

  IsLogged() {
    return localStorage.getItem("token") != null;
  }
  GetToken() {
    return localStorage.getItem("token") || '';
  }
  GetRefreshToken() {
    return localStorage.getItem("refreshtoken") || '';
  }

  SaveTokens(tokendata: any) {
    localStorage.setItem('token', tokendata.jwtToken);
    localStorage.setItem('refreshtoken', tokendata.refreshToken);
  }

  Logout() {
    alert('Your session expired')
    localStorage.clear();
    this.route.navigate(['login']);
  }

  GetRolebyToken(token: any) {
    let _token = token.split('.')[1];
    this.tokenresp = JSON.parse(atob(_token))
    return this.tokenresp.role;
  }

}
