from django.contrib import admin
from django.urls import path, include
from everything import api, web

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api.urls)),
    path('', include(web.urls)),
]
