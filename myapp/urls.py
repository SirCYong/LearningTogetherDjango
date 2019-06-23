from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<int:num>/<int:num2>", views.detail),
    path("class/", views.myapp_class),
    path('student/', views.myapp_student),
    path('class/<int:class_id>/', views.class_student),
    path('class/<int:class_id>/<int:user_id>/', views.student_info, name='student_info'),
    path('delete_student/', views.view_delete_student),
    path('add_student/', views.add_student),
    path('student_page/<int:page>/', views.student_page),
    path('hello/<num>/', views.hello_world),
]