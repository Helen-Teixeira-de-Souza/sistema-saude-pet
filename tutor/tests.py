from django.test import TestCase
from django.urls import reverse
from .models import Tutor


class TutorRegistrationTests(TestCase):
    def test_registration_page_is_public(self):
        response = self.client.get(reverse('tutor:criar'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Criar conta de tutor')

    def test_registration_creates_tutor_with_hashed_password(self):
        response = self.client.post(reverse('tutor:criar'), {
            'username': 'ana',
            'email': 'ana@example.com',
            'nome': 'Ana Silva',
            'telefone': '11999999999',
            'password1': 'UmaSenha-Forte2026!',
            'password2': 'UmaSenha-Forte2026!',
        })

        self.assertRedirects(response, reverse('login'))
        tutor = Tutor.objects.get(username='ana')
        self.assertTrue(tutor.check_password('UmaSenha-Forte2026!'))

    def test_registration_rejects_mismatched_passwords(self):
        response = self.client.post(reverse('tutor:criar'), {
            'username': 'ana',
            'email': 'ana@example.com',
            'nome': 'Ana Silva',
            'telefone': '11999999999',
            'password1': 'UmaSenha-Forte2026!',
            'password2': 'OutraSenha-Forte2026!',
        })

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Tutor.objects.filter(username='ana').exists())
