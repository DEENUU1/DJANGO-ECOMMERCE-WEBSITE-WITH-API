from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('shopcontact.urls')),
    url('', include('shop.urls', namespace='shop')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('orders/', include('cart.urls', namespace='orders')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

