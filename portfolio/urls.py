from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view, name='view'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
]