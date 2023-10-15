from django.urls import path, include
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='Project_List'),
    path('project/create', views.ProjectCreateView.as_view(), name='Project_create'),
    path('project/delete/<int:pk>',
         views.ProjectDeleteView.as_view(), name='Project_delete'),
    path('project/edit/<int:pk>',
         views.ProjectUpdateView.as_view(), name='Project_update'),
    path('task/update/<int:pk>/',
         views.ProjectUpdateView.as_view(), name='Task_update'),
    path('task/create', views.TaskCreateView.as_view(), name='Task_create'),
    path('task/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='Task_delete'),



]
