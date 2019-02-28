from django.urls import path
from . import views

# TO ROUTE PATHS TO FUNCTIONS
urlpatterns = [
    path('', views.index, name='index'),
    path('congrats/', views.congrats, name='congrats'),

]