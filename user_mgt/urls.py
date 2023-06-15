from django.urls import path

from. import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('patient/dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),    
]
