from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('reg',Regview.as_view(),name='reg'),
    path('home',Homeview.as_view(),name='home'),

    path('search',views.searchview,name='search-venus'),
    path('list',Productlistview.as_view(),name='list'),
    path('lgout',Lgoutview.as_view(),name='logout'),

]