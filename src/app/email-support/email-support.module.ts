import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { EmailSupportRoutingModule } from './email-support-routing.module';

import { EditEmailComponent } from './components/thunderbird/edit-email/edit-email.component';
import { ViewEmailComponent } from './components/thunderbird/view-email/view-email.component';


@NgModule({
  declarations: [
  
    EditEmailComponent,
    ViewEmailComponent,
  ],
  imports: [
    CommonModule,
    EmailSupportRoutingModule
  ]
})
export class EmailSupportModule { }
