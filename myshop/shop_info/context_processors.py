from .models import (
    BannerInfo,
    AboutShopDescription,
    DeliveryInfo,
    FooterDescription,
    FooterContactInfo,
    NavbarLogo,
)

# This context processors work with models and allows admin user to change some information
# That on first sight look static, but they are easily modifiable


def banner_text(request):
    banner = BannerInfo.objects.last()
    if banner:
        return {"banner_text": banner.text}
    else:
        return {"banner_text": ""}


def about_descr(request):
    about = AboutShopDescription.objects.last()
    if about:
        return {"about_desc": about.text}
    else:
        return {"about_desc": ""}


def shipping_info(request):
    info = DeliveryInfo.objects.last()
    if info:
        return {"shipping_text": info.text}
    else:
        return {"shipping_text": ""}


def footer_descr(request):
    footer_desc = FooterDescription.objects.last()
    if footer_desc:
        return {"footer_descr": footer_desc.text}
    else:
        return {"footer_descr": ""}


def footer_contact(request):
    footer_cont = FooterContactInfo.objects.last()
    if footer_cont:
        return {"footer_contact_info": footer_cont}
    else:
        return {"footer_contact_info": ""}


def navbar_logo(request):
    navbar_name = NavbarLogo.objects.last()
    if navbar_name:
        return {"navbar_log": navbar_name}
    else:
        return {"navbar_log": ""}
