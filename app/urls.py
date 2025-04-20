from django.urls import path
from app import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path('add_student/', views.add_student, name= 'add_student'),
    path('add_subject/', views.add_subject, name= 'add_subject'),
    path('add_result/', views.add_result, name= 'add_result'),
    path('view_topper/', views.view_topper, name='view_topper'),
     path('view_results/', views.view_results, name='view_results'),
]
