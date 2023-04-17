from django.contrib import admin
from django.urls import path, include

from .views import home_page, template_test


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sababa.urls')),
    path('test/', template_test)
]
