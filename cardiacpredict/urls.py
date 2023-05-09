from django.contrib import admin
from django.urls import path
from predict import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
