import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { HeaderComponent } from './components/header/header.component';
import { LoginComponent } from './components/login/login.component';
import { SidenavComponent } from './components/sidenav/sidenav.component';
import { SignupComponent } from './components/signup/signup.component';

import { CoreRoutingModule } from './core-routing.module';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MaterialModule } from '../shared/material/material.module';
import { ReactiveFormsModule } from '@angular/forms';
import { IndexComponent } from './components/index/index.component';
import { FooterComponent } from './components/footer/footer.component';


@NgModule({

  declarations: [
    LoginComponent,
    SignupComponent,
    HeaderComponent,
    SidenavComponent,
    IndexComponent,
    FooterComponent,
  ],

  imports: [
    CommonModule,
    CoreRoutingModule,
    FlexLayoutModule,
    MaterialModule,
    ReactiveFormsModule
  ],

  exports: [
    HeaderComponent,
    SidenavComponent,

    FlexLayoutModule,
    CommonModule,
    CoreRoutingModule,
    MaterialModule,
    ReactiveFormsModule
  ],

})
export class CoreModule { }
