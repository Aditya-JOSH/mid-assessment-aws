from django.contrib import admin
from django.urls import path, include
from demo_website import views
urlpatterns = [
  
    path('download',views.download,name='download'),
    path('receive_otp',views.receive_otp,name='receive_otp'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('', views.task_manager, name='task_manager'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

]