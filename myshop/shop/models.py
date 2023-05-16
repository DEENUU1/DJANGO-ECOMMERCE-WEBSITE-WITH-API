from django.db import models
from django.urls import reverse


# This class creates categories
# And joins them products


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        db_index=True,
        help_text="Put the name of your category. Capitalization does not matter",
    )

    slug = models.SlugField(
        max_length=200,
        db_index=True,
        unique=True,
        help_text="It is generating automatically. Do not change that!!!",
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


# This class creates products
# I used DecimalField here to prevent rounding prices


class Product(models.Model):
    objects = None
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100,
        db_index=True,
        help_text="You can write any name you want. It does not matter on the URL",
    )

    tag = models.CharField(
        max_length=200,
        db_index=True,
        help_text="Write product tags that allows user to search by them",
    )

    slug = models.SlugField(
        max_length=200,
        db_index=True,
        help_text="It is generating automatically. Do not change that!!!",
    )

    image = models.ImageField(
        blank=True, upload_to="media/images/", help_text="You only can choose 1 image"
    )

    description = models.TextField(
        blank=True,
        help_text="You can make your products description as long as you want.",
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])


# This model is for users to rate the product
# From 1 to 5

RATE = [
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
]

# This model allows to rate products
# User has to add his username, choose rate from 1 to 5 and write text


class ProductRate(models.Model):
    objects = None
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, blank=True)
    user_name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveIntegerField(choices=RATE)


# This model allows administrator to change the value of delivery


class Delivery(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
