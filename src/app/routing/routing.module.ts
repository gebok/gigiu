import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';;

const routes: Routes = [
  { path: '', 
    loadChildren: () => import('../core/core.module').then(m => m.CoreModule)
  },

  { path: 'email-support', 
    loadChildren: () => import('../email-support/email-support.module').then(m => m.EmailSupportModule)
  },

  { path: 'calls', 
    loadChildren: () => import('../phone-call/phone-call.module').then(m => m.PhoneCallModule)
  },
];

@NgModule({
  declarations: [],

  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],

  exports: [
    RouterModule,
  ]

})

export class RoutingModule { }
