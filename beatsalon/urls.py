from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path(r'silk/', include('silk.urls', namespace='silk'))
]
