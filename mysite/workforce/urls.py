from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('landing/', views.landing, name='landing'),
    path('profile/', views.userProfile, name='profile'),
    path('home/', views.home, name='home'),

    path('add_team/', views.addTeam, name='add_team'),
    path('sidebar/', views.sidebar, name='sidebar'),

    path('work_detail/<str:pk>', views.workDetail, name='work_detail'),

    #hub
    path('hub/', views.hub, name='hub'),
    path('edit_deliverable/<str:pk>/', views.editDeliverable, name='edit_deliverable'),
    path('delete_deliverable/<str:pk>/', views.deleteDeliverable, name='delete_deliverable'),

    #tasks
    path('tasks/', views.tasks, name='tasks'),
    path('edit_task/<str:pk>/', views.editTask, name='edit_task'),
    path('delete_task/<str:pk>/', views.deleteTask, name='delete_task'),

    #media
    path('media/', views.media, name='media'),
    path('edit_file/<str:pk>/', views.editFile, name='edit_file'),
    path('delete_file/<str:pk>/', views.deleteFile, name='delete_file'),

    path('work/', views.work, name='work'),
    path('new_work/', views.newWork, name='new_work'),
    path('edit_work/<str:pk>/', views.editWork, name='edit_work'),
    path('delete_work/<str:pk>/', views.deleteWork, name='delete_work'),

    # register, login, logout
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutFunction, name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="workforce/password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="workforce/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="workforce/password_reset_form.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="workforce/password_reset_complete.html"), name="password_reset_complete"),
]
