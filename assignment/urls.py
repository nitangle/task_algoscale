from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(template_name='signup.html'),
         name='signup'),
    path('login/', views.MyLoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'),
    path('info/', views.ListUsers.as_view(), name='info'),
    path(r'delete/(?P<pk>\d+)/$', views.DeleteUser.as_view(), name='delete_view'),
]
