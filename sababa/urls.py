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
    path('add_preferred_benefits/', views.add_preferred_benefits_view, name='add_preferred_benefits'),
    path('edit_benefits_view/<int:pk>/', views.edit_benefits_view, name='edit_benefits_view'),
    path('welfare_activity_confirmation/', views.welfare_activity_confirmation_view, name='welfare_activity_confirmation'),
    path('edit_welfare_activity_confirmation_view/<int:pk>/',
         views.edit_welfare_activity_confirmation_view, name='edit_welfare_activity_confirmation_view'),
    path('welfare_acitivity_index', views.welfare_acitivity_index_view, name='welfare_acitivity_index'),
    path('welfare_activity_update/<int:id>', views.welfare_activity_update_view, name='welfare_activity_update'),
    path('welfare_activity_update/updaterecord/<int:id>',
         views.welfare_activity_updaterecord_view, name='welfare_activity_updaterecord'),
    path('table_list/', views.table_list_view, name='table_list'),
    path('display_table/', views.display_table_view, name='display_table'),
]
