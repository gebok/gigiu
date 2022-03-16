import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PhoneCallCreateEditComponent } from './components/phone-call-create-edit.component';
import { PhoneCallViewComponent } from './container/phone-call-view.component';
import { PhoneCallRoutingModule } from './phone-call-routing.module';
import { PhoneCallService } from './services/phone-call.service';

@NgModule({
  declarations: [  
    PhoneCallCreateEditComponent,
    PhoneCallViewComponent
  ],
  
  imports: [
    CommonModule,

    PhoneCallRoutingModule,
  ],

  exports : [
    PhoneCallCreateEditComponent,
    PhoneCallViewComponent
  ],

  providers: [
    PhoneCallService
  ],

})

export class PhoneCallModule { }
