from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hospitals.urls")),
    path("", include("boundaries.urls")),
]

admin.site.site_header = "Hospitals Admin"
admin.site.site_title = "Rwanda GIS Admin Portal"
admin.site.site_title = "Welcome to Rwanda GIS Portal"
