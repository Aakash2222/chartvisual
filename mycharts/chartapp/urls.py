from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.index, name='indexpage'),
     path('login', views.login, name='login'),
     path('signup/', views.signup, name='signup'),
     path('save_json', views.save_json, name='save_json'),
     path('search/', views.search, name='search'),
     path('filter-page/', views.filter, name='filter-page'),
     path('add_data/', views.add_data, name='add_data'),

]
 