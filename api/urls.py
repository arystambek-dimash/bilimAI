from django.urls import path
from . import views
from .views import TestCreateView

app_name = "api"

urlpatterns = [
    path('sign-up/', views.UserRegistrationView.as_view(), name='register'),
    path('accounts/profile/', views.UserProfileView.as_view(), name='profile'),
    path('chat/', views.ChatQueryView.as_view()),
    path('chat/history/', views.ChatHistoryAll.as_view()),
    path('chat/history/<int:pk>/delete/', views.ChatHistoryDetailDelete.as_view()),
    path('test/', TestCreateView.as_view(), name='create-test'),
    path("courses/", views.CoursesListView.as_view()),
    path("courses/upload/", views.CourseQueryView.as_view()),
    path("courses/<int:pk>/detail", views.CourseDetailView.as_view()),
    path("courses/<int:pk>/videos/", views.CourseVideosView.as_view(),name="videos"),
    path("courses/<int:pk>/videos/post-video/", views.CourseVideoQueryView.as_view()),
    path("courses/<int:pk>/videos/<int:video_id>/", views.CourseVideoDetail.as_view()),
    path("courses/<int:pk>/videos/<int:video_id>/delete/",views.CourseVideoDeleteView.as_view()),
    path("courses/<int:pk>/videos/<int:video_id>/update/", views.CourseUpdateView.as_view()),
]
