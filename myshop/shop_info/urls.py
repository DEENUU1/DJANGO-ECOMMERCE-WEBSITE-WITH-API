from django.urls import path
from . import views

app_name = 'shop_info'

urlpatterns = [
    # This url is to display about page
    path('about/', views.about, name='about_us'),

    # This url is to display page with statute
    path('statute/', views.statute, name='statute'),

    # This url is to display page with privacy_policy
    path('privacy/', views.privacy_policy, name='privacy'),

    # This url is to display shipping info
    path('shipping/', views.shipping, name='shipping'),

    # This url is to display returns and complaints info
    path('returns/', views.returns_complaints, name='returns'),

    # This url is to display faq
    path('faq/', views.faq, name='faq'),

    # This url is to display admin user all available api
    path('api', views.main_api, name='main_api')
]
