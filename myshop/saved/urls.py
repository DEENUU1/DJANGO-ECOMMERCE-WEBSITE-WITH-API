from django.urls import path
from . import views

app_name = 'saved'

urlpatterns = [
    # This url represent main side of product list of fav products

    path('', views.saved_detail, name='saved_detail'),

    # This url doesn't have temolate
    # It's only display as a function

    path('add/<int:product_id>/', views.saved_add, name='saved_add'),

    # This url doesn't have template
    # It's only display as a function

    path('remove/<int:product_id>/', views.saved_remove, name='saved_remove'),
]
