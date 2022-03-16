import { Component, OnInit } from '@angular/core';

/** Custom imports */
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { LoginComponent } from 'src/app/login/components/login.component';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  public signupForm!: FormGroup;

  constructor(
    private dialog: MatDialog,
    private fb: FormBuilder, 
    private http: HttpClient, 
    private router: Router
  ) { }

  ngOnInit(): void { 
    this.signIn();
  }

  signIn(): void {
    this.signupForm = this.fb.group({
      fullname: ['', Validators.required],
      mobile: ['', Validators.required],
      email: ['', Validators.required],
      password: ['', Validators.required]
    })
  }

    signUp(): void {
    this.http.post<any>("http://localhost:3000/signupUsers", this.signupForm.value)
    .subscribe ({
      next: res => {
        alert("Signup successfull");
        this.signupForm.reset();
        this.router.navigate(['login']);
      },
      error: (err) => {
        alert("Something went wrong!");
      }
    })
  }

  login(): void {
    this.dialog.open(LoginComponent);
  }

}
