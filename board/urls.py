from django.urls import path
from . import views

urlpatterns=[
    path('notice/', views.notice_list, name='notice_list'),
    path('contact/', views.contact_list, name='contact_list'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/new/', views.post_new, name='post_new'),
    path('contact/<int:pk>/reply/', views.replyContact, name='replyContact'),
    path('contact_list/', views.mypage_contact_list, name='mypage_contact_list'),
]
