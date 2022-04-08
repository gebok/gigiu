import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { Call } from '../models/call';

@Injectable({
  providedIn: 'root'
})

export class PhoneCallService {

  private apiURL = "http://localhost:8000/calls/";

  httpOptions = { headers: new HttpHeaders({
    'Content-type': 'application/json'
    })
  }

  constructor(
    private http: HttpClient,
  ) {}


  /**
   * getAll() Method
   * @return response()
   */
  getAll(): Observable<any> {
    return this.http.get(this.apiURL).pipe(catchError(this.errorHandler));
  }

  /**
   * errorHandler() Method
   * @returns response()
   */
  errorHandler(error: any) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      errorMessage = error.error.message;
    } else {
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    return throwError(errorMessage);
  }
}
