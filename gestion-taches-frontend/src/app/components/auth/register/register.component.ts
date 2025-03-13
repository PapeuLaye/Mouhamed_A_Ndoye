import { Component } from '@angular/core';
import { AuthService } from '../../../services/auth.service';
import { Router, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule, ReactiveFormsModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  userData = { username: '', email: '', password: '', type_utilisateur: 'etudiant' };
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {}

  register() {
    this.authService.register(this.userData).subscribe({
      next: () => {
        this.router.navigate(['/login']); // Redirige vers la connexion après inscription
      },
      error: () => {
        this.errorMessage = "Erreur lors de l'inscription";
      }
    });
  }
}
