from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shopcontact.urls')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('cart.urls', namespace='orders')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls', namespace='payment')),
    url('', include('shop.urls', namespace='shop')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

