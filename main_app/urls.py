from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_index, name='project_index'),
    path('projects/<int:project_id>', views.project_details, name='project_details'),
    path('projects/create', views.ProjectCreate.as_view(), name='project_create'),
    path('projects/<int:pk>/update', views.ProjectUpdate.as_view(), name='project_update'),
    path('projects/<int:pk>/delete', views.ProjectDelete.as_view(), name='project_delete'),
    path('bugs/create', views.BugCreate.as_view(), name='bug_create'),
    path('bugs/', views.bug_index, name='bug_index'),
    path('bugs/<int:bugs_id>', views.bug_details, name='bug_details'),
    path('bugs/filtered/', views.bug_filtered, name='bug_filtered'),
    path('bugs/<int:pk>/update', views.BugUpdate.as_view(), name='bug_update'),
    path('bugs/<int:pk>/delete', views.BugDelete.as_view(), name='bug_delete'),
    path('accounts/register/', views.register, name='register'),
    path('bugs/<int:bugs_id>/assignuser/<int:user_id>/', views.assign_user, name='assign_user'),
    path('bugs/<int:bugs_id>/unassignuser/<int:user_id>/', views.unassign_user, name='unassign_user'),
]