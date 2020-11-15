from django.urls import path
from .views import firstpg, signin, project, profile

urlpatterns = [
    path('', firstpg, name='firstpg'),
    path('signin/', signin, name='signin'),
    path('project/', project, name='project'),
    path('profile/', profile, name='profile'),
]
