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
    path('hello/', views.hello_world),
    path('attribute/', views.attribute),
    path('attribute/get1/', views.attribute_get1),
    path('attribute/get2/', views.attribute_get2),
    path('show_register/', views.show_register),
    path('show_register/register/', views.register),
    path('show_response/', views.show_response),
    path('show_cookie/', views.show_cookie),
    path('show_redirect1/', views.show_redirect1),
    path('show_redirect2/', views.show_redirect2),


]