# quiz/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'quiz'

urlpatterns = [
    # Home and Registration
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='quiz:home'), name='logout'),

    # Quiz
    path('quiz/start/', views.start_quiz, name='start_quiz'),
    path('quiz/question/', views.get_quiz_question, name='get_question'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
]

