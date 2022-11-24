from django.urls import path
from . import views

urlpatterns=[
    path('terms/', views.terms, name='terms'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_list_detail/<str:mb_id>/', views.user_list_detail, name='user_list_detail'),
    path('profile/', views.mypage_profile, name='mypage_profile'),
    path('modify_profile/', views.modify_profile, name='modify_profile'),
    path('check_pw/<int:sort>/', views.check_pw, name='check_pw'),
    path('unregister/', views.mypage_unregister, name='mypage_unregister'),
    path('modify/<int:sort>/', views.mypage_modify, name='mypage_modify'),
]
