
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ai_interview_options/', views.ai_interview_options, name='ai_interview_options'),
    path('login/', views.login_view, name='login'),
    path('candidate_signup/', views.candidate_signup, name='candidate_signup'),
    path('recruiter_signup/', views.recruiter_signup, name='recruiter_signup'),
    path('candidate_dashboard/', views.candidate_dashboard, name='candidate_dashboard'),
    path('recruiter_dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('candidate_profile/', views.candidate_profile, name='candidate_profile'),
    path('manage_jobs/', views.manage_jobs, name='manage_jobs'),
    path('explore_jobs/', views.explore_jobs, name='explore_jobs'),
    path('apply_job/<str:job_id>/', views.apply_job, name='apply_job'),
    path('view_candidates/', views.view_candidates, name='view_candidates'),
    path('schedule_interview_direct/<str:job_id>/<str:candidate_email>/', views.schedule_interview_direct, name='schedule_interview_direct'),
    path('mixed_interview/', views.mixed_interview, name='mixed_interview'),
    path('technical_interview/', views.technical_interview, name='technical_interview'),
    path('general_interview/', views.general_interview, name='general_interview'),
    path('index/<str:interview_type>/', views.index, name='index'),
    path('question/<str:interview_type>/', views.question, name='question'),
    path('results/', views.results, name='results'),
    path('video_feed/', views.video_feed, name='video_feed'),
]