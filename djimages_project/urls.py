from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 

from inmuebles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inmueble_view, name='blog'),
    path('<int:id>/', views.detail_view, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)