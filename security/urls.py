from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, forms

#app_name = 'security'

urlpatterns = [
    path('signup/', views.signup_user_view, name='signup'),
    path('', views.AppLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    path('profile/<int:id>', views.AppUserProfile.as_view(), name='user_profile_view'),
    path('update_appuser/<int:pk>', views.AppUserUpdateView.as_view(), name='update_appuser'),


    path('join/', views.JoinFormView.as_view(), name='login2'),
    path('index/', views.index, name='index'),
]