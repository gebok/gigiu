import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from 'src/app/app.component';

/** Custom imports */
import { FlexLayoutModule } from '@angular/flex-layout';
import { HttpClientModule } from '@angular/common/http';
import { MaterialModule } from 'src/app/material/material.module';
import { ReactiveFormsModule } from '@angular/forms';
import { RoutingModule } from './routing/routing.module';

import { environment } from '../environments/environment';
import { LoginModule } from './login/login.module';
import { PhoneCallModule } from './phone-call/phone-call.module';
import { SignupComponent } from './signup/signup.component';
import { StoreModule } from '@ngrx/store';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent
  ],

  imports: [
    BrowserAnimationsModule,
    BrowserModule,
    FlexLayoutModule,
    ReactiveFormsModule,
    HttpClientModule,
    LoginModule,
    MaterialModule,
    RoutingModule,
    StoreModule.forRoot({}, {}),
    StoreDevtoolsModule.instrument({ maxAge: 25, logOnly: environment.production, autoPause: true}),
    PhoneCallModule,
  ],

  exports: [
    BrowserModule,
    BrowserAnimationsModule,
    FlexLayoutModule,
    ReactiveFormsModule,
    HttpClientModule,
    LoginModule,
    MaterialModule,
    RoutingModule
  ],

  providers: [],
  bootstrap: [AppComponent]
})

export class AppModule { }
