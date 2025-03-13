import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiURL = 'http://127.0.0.1:8000/api'; // URL du backend Django

  constructor(private http: HttpClient, private router: Router, private jwtHelper: JwtHelperService) {}

  login(credentials: any) {
    return this.http.post(`${this.apiURL}/token/`, credentials);
  }

  register(userData: any) {
    return this.http.post(`${this.apiURL}/register/`, userData);
  }

  logout() {
    localStorage.removeItem('token');
    this.router.navigate(['/login']);
  }

  isLoggedIn(): boolean {
    const token = localStorage.getItem('token');
    return token ? !this.jwtHelper.isTokenExpired(token) : false;
  }
}
