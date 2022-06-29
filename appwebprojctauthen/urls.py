from unicodedata import name
from django import views
from django.urls import include, path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('user_login/',views.user_login,name='user_login'),
    path('about/',views.about,name='about'),
    path('usercreate/',views.usercreate,name="usercreate"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('addcourse',views.addcourse,name="addcourse"),
    path('add_course',views.add_course,name="add_course"),
    path('addstudent',views.addstudent,name="addstudent"),
    path('add_student_details',views.add_student_details,name="add_student_details"),
    path('showstudent',views.showstudent,name="showstudent"),
]
