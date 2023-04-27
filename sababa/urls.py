from django.urls import path

from . import views

urlpatterns = [
    path('add_welfare_activity', views.add_welfare_activity_request_view, name='add_welfare_activity_request'),
    path('add_employee', views.add_employee_view, name='add_employee_view'),
    path('update_employee_perm', views.update_employee_perm, name='update_employee_perm'),
    path('add_happyhour_package', views.add_new_happy_hour_package, name='add_new_happy_hour_package'),
    path('event_register', views.register_to_event, name='event_register'),
    path('choose_holiday_gift', views.choose_holiday_gift, name='choose_holiday_gift'),
    path('choose_birthday_gift', views.choose_birthday_gift, name='choose_birthday_gift'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
