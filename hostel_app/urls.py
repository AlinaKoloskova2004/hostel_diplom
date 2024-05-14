from django.urls import path
from hostel_app.views import HostelAppView, HostelAppView2, restaurant_view, room_id_view
from . import views


app_name = 'hostel_app'

urlpatterns=[
    path('', HostelAppView.as_view(), name='hostel_app'),
    path('room/', HostelAppView2.as_view(), name='rooms'),
    path('restaurant/', views.book_room, name='booking'),
    path('booking/', restaurant_view, name='restaurant'),
    path('<int:pk>/', room_id_view, name='details'),
    path('profile_user/',  views.view_profile, name='profile_user'),
    path('profile_user/edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile_user/create_profile/', views.create_profile, name='create_profile'),
    path('profile_user/create_profile/success', views.success, name='success'),
]
