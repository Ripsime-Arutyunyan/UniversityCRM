from django.urls import path
from .import  views

urlpatterns=[
     path('',views.accounts_home, name='home'),
     path('register/',views.register, name='register'),
     path('student_register/',views.student_register.as_view(), name='student_register'),
     path('teacher_register/',views.teacher_register.as_view(), name='teacher_register'),
     path('admin_register/',views.admin_register.as_view(), name='admin_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]