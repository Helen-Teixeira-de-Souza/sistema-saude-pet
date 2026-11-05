from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutor.urls')),
    path('pet/', include('pet.urls')),
    path('tutor/', include('tutor.urls')),
    path('vacinacao/', include('vacinacao.urls')),
    path('vacina/', include('vacina.urls')),
    path('cirurgia/', include('cirurgia.urls')),
    path('medicamento/', include('medicamento.urls')),
    path('consulta/', include('consulta.urls')),
    path('exame/', include('exame.urls')),
    path('profissional/', include('profissional.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='accounts_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Rotas para redefinição de senha
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), 
         name="reset_password"),
         
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
         name="password_reset_done"),
         
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), 
         name="password_reset_confirm"),
         
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), 
         name="password_reset_complete"),
]
