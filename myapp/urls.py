from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.ProjectListView.as_view(),name='Project_List'),
    path('project/creats',views.ProjectCreateView.as_view(),name='Project_create') 
]
