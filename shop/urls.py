from django.urls import path
from . import views

urlpatterns = [
    path('plant/', views.plant_list, name='plant_list'),
    path('plant/foliage/', views.plant_list_1, name='plant_list_1'),
    path('plant/succulent/', views.plant_list_2, name='plant_list_2'),
    path('plant/bulbous/', views.plant_list_3, name='plant_list_3'),
    path('plant/herb/', views.plant_list_4, name='plant_list_4'),
    path('plant/cactus/', views.plant_list_5, name='plant_list_5'),
    path('plant/detail/<int:id>/', views.plant_detail, name='plant_detail'),
    path('plant/buy/', views.plant_buy, name='plant_buy'),
    path('plant/cart/', views.plant_cart, name='plant_cart'),
    path('plant/buy/order/', views.plant_order, name='plant_order'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('confirm_order/detail/<int:id>/', views.order_detail, name='order_detail'),
    path('confirm_order/cancel/', views.cancel_order, name='cancel_order'),
    path('statsCheck/', views.statsCheck, name='statsCheck'),
    path('admin_plantList/', views.admin_plantList, name='admin_plantList'),
    path('admin_plantList/detail/<int:pl_id>/', views.admin_plantList_detail, name='admin_plantList_detail'),
    path('admin_orderList/', views.admin_orderList, name='admin_orderList'),
    path('admin_orderList/detail/<int:order_id>/', views.admin_orderList_detail, name='admin_orderList_detail'),
    path('admin_orderItemList/', views.admin_orderItemList, name='admin_orderItemList'),
    path('admin_cartList/', views.admin_cartList, name='admin_cartList'),
    path('statsCheck/detail/<int:id>/', views.statsCheck_detail, name='statsCheck_detail'),
    path('check_pw_sub/', views.check_pw_sub, name='check_pw_sub'),
]
