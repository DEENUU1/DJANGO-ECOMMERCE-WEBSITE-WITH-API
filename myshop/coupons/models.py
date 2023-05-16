from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# This model allows to create coupons
# The coupons have name, rabat price, date
class Coupon(models.Model):
    code = models.CharField(max_length=100, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    active = models.BooleanField()

    def __str__(self):
        return self.code
