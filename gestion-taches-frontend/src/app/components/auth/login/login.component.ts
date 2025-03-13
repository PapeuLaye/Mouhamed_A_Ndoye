import { Component } from '@angular/core';
import { AuthService } from '../../../services/auth.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms'; // ✅ Nécessaire pour `ngModel`
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule] // ✅ Ajoute les modules nécessaires
})
export class LoginComponent {
  credentials = { username: '', password: '' };
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {}

  login() {
    this.authService.login(this.credentials).subscribe({
      next: (response: any) => {
        localStorage.setItem('token', response.access); // Stocke le token
        this.router.navigate(['/dashboard']); // Redirige vers le tableau de bord
      },
      error: () => {
        this.errorMessage = 'Identifiants incorrects';
      }
    });
  }
}
