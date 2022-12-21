from django.db import models
from django.urls import reverse
from star_ratings.models import AbstractBaseRating


# This class creates categories
# And joins them products
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True,
                            help_text='Put the name of your category. Capitalization does not matter')
    slug = models.SlugField(max_length=200, db_index=True, unique=True,
                            help_text='It is generating automatically. Do not change that!!!')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])

# This class creates products
# I used DecimalField here to prevent rounding prices
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True,
                            help_text='You can write any name you want. It does not matter on the URL')
    slug = models.SlugField(max_length=200, db_index=True,
                            help_text='It is generating automatically. Do not change that!!!')
    image = models.ImageField(blank=True, upload_to='media/images/',
                              help_text='You only can choose 1 image')
    description = models.TextField(blank=True,
                                   help_text='You can make your products description as long as you want.')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


# This model is for users to write a comments
# All user can write a comment after adding name, subject and email
# It doens't work now!
# class Comments(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user_name = models.CharField(max_length=30)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#     email = models.EmailField()
#     subject = models.CharField(max_length=100)
#
#     def __str__(self):
#         return '%s - %s' % (self.product.name, self.user_name)
#
