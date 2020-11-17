from django.urls import path
from .views import firstpg, signup, project, profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', firstpg, name='firstpg'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('project/', project, name='project'),
    path('profile/', profile, name='profile'),
]
