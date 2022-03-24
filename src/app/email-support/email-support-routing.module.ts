import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { EditEmailComponent } from './components/thunderbird/edit-email/edit-email.component';
import { ViewEmailComponent } from './components/thunderbird/view-email/view-email.component';

const routes: Routes = [
  { path: '', component: ViewEmailComponent },
  { path: 'edit-email', component: EditEmailComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EmailSupportRoutingModule { }
