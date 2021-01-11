from django.urls import path
from .views import firstpg, signup, project, mypage, SetPlan
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', firstpg, name='firstpg'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('project/', project, name='project'),
    path('mypage/', mypage, name='mypage'),
    path('project_detail/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('setplan/', SetPlan, name='setplan'),
]
