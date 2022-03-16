import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PhoneCallCreateEditComponent } from './components/phone-call-create-edit.component';

import { PhoneCallViewComponent } from './container/phone-call-view.component';

const routes: Routes = [
  { path: 'calls', component: PhoneCallViewComponent },
  { path: 'calls/create-edit', component: PhoneCallCreateEditComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PhoneCallRoutingModule { }
