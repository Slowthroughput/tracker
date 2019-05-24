from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:engagement_id>/', views.view_engagement, name='view'),
    path('<int:engagement_id>/hosts/', views.view_host, name='hosts'),
    path('<int:engagement_id>/credentials/', views.view_creds, name='credentials')
]