from django import views
from django.contrib import admin
from django.urls import path
from artapp.views import HomePageView, AdminLoginView, ArticlesView, create_superuser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('create-superuser/', create_superuser, name='admin-create-superuser'),
    
]
