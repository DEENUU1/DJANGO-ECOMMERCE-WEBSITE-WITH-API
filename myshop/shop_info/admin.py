from django.contrib import admin
from .models import (
    BannerInfo,
    AboutShopDescription,
    DeliveryInfo,
    FooterDescription,
    FooterContactInfo,
    NavbarLogo,
)

admin.site.register(BannerInfo)
admin.site.register(AboutShopDescription)
admin.site.register(DeliveryInfo)
admin.site.register(FooterDescription)
admin.site.register(FooterContactInfo)
admin.site.register(NavbarLogo)
