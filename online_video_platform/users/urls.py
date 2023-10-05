from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/register/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='users/signout.html'), name='signout'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', views.UpdateProfile.as_view(), name='update_profile')
]
