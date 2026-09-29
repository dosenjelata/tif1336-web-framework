from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls')),
    path('about/', views.about, name='about'),  # Menambahkan URL untuk halaman About
]
