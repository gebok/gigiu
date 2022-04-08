import { Component, OnInit, ViewChild } from '@angular/core';

import { Call } from '../models/call';
import { PhoneCallService } from '../services/phone-call.service';
import { Table } from 'primeng/table';
import { PrimeNGConfig } from 'primeng/api';


@Component({
  selector: 'app-phone-call-view',
  templateUrl: './phone-call-view.component.html',
  styleUrls: ['./phone-call-view.component.scss']
})
export class PhoneCallViewComponent implements OnInit {

  calls!: Call[];

  selectedCalls!: Call[];

  loading: boolean = true;

  @ViewChild('dt') table!: Table;

  constructor (
    private phoneCallService: PhoneCallService, 
    private primengConfig: PrimeNGConfig
  ) { }

  ngOnInit(): void {
    this.getAllCalls();
  }

  getAllCalls(): void {
    this.phoneCallService.getAll().subscribe((calls: any) => {
      this.calls = calls;
      this.loading = false;
      console.log(calls);
    })
  }
  
}