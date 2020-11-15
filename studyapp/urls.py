from django.urls import path
from .views import firstpg, login, logout, project, profile

urlpatterns = [
    path('', firstpg, name='firstpg'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('project/', project, name='project'),
    path('profile/', profile, name='profile'),
]
