from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.test_main, name='test_main'),
    path('result/', views.test_result, name='test_result'),
    path('result/All/', views.test_result_list, name='test_result_list'),
    path('test_introduce/', views.test_introduce, name='test_introduce'),
]
