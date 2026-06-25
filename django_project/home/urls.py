from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    # FIX: Pointed this to views.doctors instead of views.doc
    path('doctors/', views.doctors, name='doctors'), 
    path('department/', views.dept, name='dept'),
    path('booking/', views.booking, name='booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('booking/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup, name='signup'),
]