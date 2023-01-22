
# DJANGO ECOMMERCE WEBSITE 

It is a fully functional website for online sales. 

It was written in Django and uses the Django Rest Framework.

It has many functionalities such as: writing product reviews, adding to the basket,
payments via PayPal, writing messages, creating user accounts and many others. 
All functions are included in the documentation.

The most difficult part of the project was adding the payment gateway.
Payments work fine but are not perfect. In future updates they will be improved to be more efficient


## Demo

- [VIDEO DEMO ON YOUTUBE](https://youtu.be/LnE373sdkd0)


## Features

- Improve cart and order function 
- Add choice of delivery options

## Installation

Install my-project with npm

```bash
Clone this repository on your local machine
  > git clone <link>

Go to the main file 
  > cd myshop

Install files from requirements
  > pip install -r requirements.txt

Makemigrations and migrate 
  > py manage.py Makemigrations
  > py manage.py migrate

Create super user
  > py manage.py createsuperuser

Run server
  > py manage.py runserver
```

## How to use
### This is only a simple configuration. For full configuration go here: https://www.youtube.com/

1. First go to admin panel 127.0.0.1:8000/admin

Here you can add new category, products
See all orders, PayPal IPNS, product rates and messages from the users

### ADDING NEW PRODUCT/CATEGORY

Go to Product and click ADD PRODUCT
Create category if you don't have any others.

Add name it will automatically generate Slug.

Then add some Tags. It really important because it optimizes searching process.

Add image and write product description

Then add price and stock. Do not add 0 in Stock because it will automatically make this product unavailable

After all click SAVE button.

Now you can go to the main page and see your product on the website.

Remember if AVAILABLE won't be checked it won't show up on the main page.



### ADDING COUPONS 

Go to Coupons, and click ADD COUPON

Add some code that user will have to write to get a rabat

Add date during which the coupon will be active

And add value of Discount as a number (1-100) this value is expressed as a percentage

And mark Active 


## API Reference

#### All available API

```http
  127.0.0.1:8000/shop_info/api
```

On this url are displayed links for all available API:
- Product data
- Category data
- Coupon data
- Order data
- Order Item data
- Product ADD
- Category ADD
- Coupon ADD

This informations are 
## Authors

- [@DEENUU1](https://www.github.com/DEENUU1)


## License

[MIT](https://choosealicense.com/licenses/mit/)

