import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

/** Custom imports */
import { LoginModule } from 'src/app/login/login.module';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from 'src/app/login/components/login.component';
import { SignupComponent } from 'src/app/signup/signup.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent },
  // { path: 'calls', loadChildren: () => import ('../phone-call/phone-call.module').then(a => a.PhoneCallModule), canActivate: [Log] }
];

@NgModule({
  declarations: [],

  imports: [
    CommonModule,

    LoginModule,
    RouterModule.forRoot(routes)
  ],

  exports: [
    LoginModule,
    RouterModule
  ]

})
export class RoutingModule { }
