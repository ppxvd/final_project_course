from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = 'auth_comments_app'

urlpatterns = [
    path('create_account/', views.create_account, name='create_account'),
    path('login/', LoginView.as_view(template_name='auth_comments_app/login.html'), name='login'),

]
