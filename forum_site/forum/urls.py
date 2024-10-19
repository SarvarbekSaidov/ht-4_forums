from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('update_topic/<int:pk>/', views.update_topic, name='update_topic'),
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('', views.home, name='home'),
]
