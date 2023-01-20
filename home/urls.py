from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('sorting/<str:algorithm>', views.sorting, name='sorting'),
]