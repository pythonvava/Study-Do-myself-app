from django.urls import path
from .views import firstpg_func, signup_func, signin_func, makeproject_func, profile_func

urlpatterns = [
    path('', firstpg_func, name='firstpg'),
    path('signup/', signup_func, name='signup'),
    path('signin/', signin_func, name='signin'),
    path('makeproject/', makeproject_func, name='makeproject'),
    path('profile/', profile_func, name='profile'),
]
