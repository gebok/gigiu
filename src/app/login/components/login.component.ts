import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

/** Custom imports */
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { Router } from '@angular/router';

// import { LoginAuthService } from '../services/loginAuth.service';
import { SignupComponent } from '../../signup/signup.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  public loginForm!: FormGroup;
  responsedata: any;

  constructor(
    private dialog: MatDialog,
    private fb: FormBuilder,
    private http: HttpClient,
    private route: Router,
    // private loginAuthService: LoginAuthService
  ) { 
    localStorage.clear(); 
  }

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      email: ['', Validators.required],
      password: ['', Validators.required]
    })
  }

  // login(){
  //   if(this.loginForm.valid){
  //     this.loginAuthService.proceedLogin(this.loginForm.value)
  //     .subscribe(result => {
  //       this.responsedata = result;
  //       if(this.responsedata != null){
  //         localStorage.setItem('token', this.responsedata.jwtToken);
  //         this.route.navigate(['calls/create-edit']);
  //       } else {
  //         alert('Login Failed!')
  //       }
  //     });
  //   }    
  // }

  login(){
    this.http.get<any>("http://localhost:3000/signupUsers")
    .subscribe(result => {
      next: {
      this.responsedata = result;
        const user = this.responsedata.find((a: any) => {
          return a.email === this.loginForm.value.email && a.password === this.loginForm.value.password;
        })
        if(this.responsedata != null && user) {
          alert("Login success!");
          this.loginForm.reset();
          this.route.navigate(['calls/create-edit']);
        } else {
          alert("User not found");
        }
      }
      error: () => {
        alert("Something went wrong");
      }
    })
  }


  signIn(): void {
    this.dialog.open(SignupComponent);
  }

}