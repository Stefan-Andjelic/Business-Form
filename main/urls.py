from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('share/', views.post_share, name='post_share'),
]
