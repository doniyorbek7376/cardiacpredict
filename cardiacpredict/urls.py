from django.contrib import admin
from django.urls import path, include
from predict import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from rest_framework import routers
from predict import views


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('profile/', views.profile_view, name="profile"),
    path('logout/', views.logout_view, name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/predict', views.PredictAPI.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
