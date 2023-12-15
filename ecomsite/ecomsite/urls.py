
from django.contrib import admin
from django.urls import path
from .views import home
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('store/',include('store.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
