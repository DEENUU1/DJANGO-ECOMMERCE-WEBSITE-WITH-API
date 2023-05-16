from django.db import models

# This models allows to edit "static" information in admin panel
# It works with context_processors

# Changing text in baner under navigation bar


class BannerInfo(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


# Changing shop description on page /shop_info/about


class AboutShopDescription(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


# Changing delivery information on page /shop_info/shipping


class DeliveryInfo(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


# Change shop description in footer


class FooterDescription(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text


# Change contact information in footer


class FooterContactInfo(models.Model):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email


# Change the shop name in navigation bar


class NavbarLogo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
