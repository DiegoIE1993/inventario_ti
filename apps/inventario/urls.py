from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#from inventarios.views import prueba

urlpatterns = [
    #path("dashboard/", views.dashboard, name="dashboard"),
    #path('login', views.login, name="login"),
    
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
  
    
]