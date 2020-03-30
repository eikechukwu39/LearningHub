from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('topics/', views.topics, name='topics'),
]
