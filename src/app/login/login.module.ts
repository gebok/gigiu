import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReactiveFormsModule } from '@angular/forms';
import { LoginComponent } from './components/login.component';
import { LoginAuthService } from './services/loginAuth.service';
import { MaterialModule } from '../material/material.module';



@NgModule({
  declarations: [
    LoginComponent
  ],

  imports: [
    CommonModule,

    MaterialModule,
    ReactiveFormsModule
  ],

  exports: [
    MaterialModule,
    ReactiveFormsModule
  ],

  providers: [
    LoginAuthService,
  ],

})
export class LoginModule { }
