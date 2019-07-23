from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('silk/', include('silk.urls', namespace='silk'))
]
