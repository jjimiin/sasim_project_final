from django.urls import path
from . import views

urlpatterns=[
    path('main/', views.mypage_main, name='mypage_main'),
    path('order_success/', views.order_success, name='order_success'),
    path('admin_order_check/<int:sort>/', views.admin_order_check, name='admin_order_check'),
]
