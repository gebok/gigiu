import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReactiveFormsModule } from '@angular/forms';
import { LoginAuthService } from './services/loginAuth.service';
import { MaterialModule } from '../material/material.module';

import { LoginComponent } from './components/login.component';


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
