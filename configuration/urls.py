from django.urls import path
from . import views


app_name = 'configuration'

urlpatterns = [

    path('', views.configuration, name='configuration'),
    path('users', views.users, name='users'),
    path('create_group/', views.GroupCreateView.as_view(), name='create_group'),
    

]

