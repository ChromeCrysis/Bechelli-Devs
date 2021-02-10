from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
admin.autodiscover()

urlpatterns = [
	path('admin/', admin.site.urls, name='admin'),
	path('', views.index, name='index'),
	path('home/', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)