from django.urls import path
from . import views

app_name = 'shop_info'

urlpatterns = [
    # This url is to display about page
    path('about/', views.about, name='about_us'),

    # This url is to display shipping info
    path('shipping/', views.shipping, name='shipping'),

    # This url is to display all documents
    path('documents', views.all_documents, name='all_documents'),

    # This url is to display faq
    path('faq/', views.faq, name='faq'),

    # This url is to display admin user all available api
    path('api', views.main_api, name='main_api')
]
