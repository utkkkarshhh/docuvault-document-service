from django.contrib import admin
from django.urls import path, include

from service.view import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('api/v1/', include('service.urls')),
]
