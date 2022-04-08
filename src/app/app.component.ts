import { Component, OnInit, ViewChild } from '@angular/core';
import { PrimeNGConfig } from 'primeng/api';

/** Custom imports */
import { BreakpointObserver } from '@angular/cdk/layout';
import { delay } from 'rxjs/operators';
import { MatSidenav } from '@angular/material/sidenav';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {

  title = 'gigiu';

  @ViewChild(MatSidenav) sidenav!: MatSidenav;

  constructor(
    private observer: BreakpointObserver ,
    private primeNGConfig: PrimeNGConfig,
    ) {}

    ngOnInit(){
      this.primeNGConfig.ripple = true;
    }

  ngAfterViewInit() {
  //   this.observer.observe(['(max-width: 600px)'])
  //   .pipe(delay(1))
  //   .subscribe((res) => {
  //     if(res.matches) {
  //       this.sidenav.mode = 'over';
  //       this.sidenav.close();
  //     } else {
  //       this.sidenav.mode = 'side';
  //       this.sidenav.open();
  //     }
  //   });
  }
}