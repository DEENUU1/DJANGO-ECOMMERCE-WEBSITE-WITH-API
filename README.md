
# DJANGO ECOMMERCE WEBSITE

This is an online store design.\
Created with Django, Django Rest Framework, HTML, CSS, JS.
It has functionalities such as:
- Adding: products, categories, discount coupons
- Adding products to the cart
- Payments via PayPal
- Registration, login, password change, user account deletion
- Writing comments, rating products
- API created with Django Rest Framework
- Sending emails when registering, changing password and creating an order
- And a lot more

The most difficult part of this project was integrating the payment system, as well as creating a shopping cart based on SOLID principles.
## Demo
- [VIDEO DEMO ON YOUTUBE](https://youtu.be/LnE373sdkd0)

<img src="/files/2.png"/>
<img src="/files/3.png"/>
<img src="/files/4.png"/>
<img src="/files/5.png"/>

## Features

- Improve cart and order function
- Add choice of delivery options

## Installation and configuration

Install my-project with npm

Clone this repository on your local machine
```bash
  > git clone <link>
```
Go to the main file
```bash
  > cd myshop
```

Install files from requirements
```bash
  > pip install -r requirements.txt
```

Makemigrations and migrate
```bash
  > py manage.py makemigrations
  > py manage.py migrate
```

Create super user
```bash
  > py manage.py createsuperuser
```

Run server
```bash
  > py manage.py runserver
```

## How to use
### This is only a simple configuration. For full configuration go here: - [Full configuration](https://youtu.be/LnE373sdkd0)

First go to admin panel 127.0.0.1:8000/admin

<img src="/files/1.png"/>

### Inside Admin Panel you can easely:

#### Crud operations:
- Add product
- Add category
- Add coupons
- Add delivery price


#### Browsing informations:
- Registered users
- PayPal IPNS
- Orders
- Product rates
- Messages from customers

#### Editing most "static" value
- Description about shop
- Information which is displaying on the baner under the navigation bar
- Information about delivery
- Footer information
- Navigation bar logo


### Project configuration

#### How to use ngrok

Ngrok allows you to create server on your local machine. It is really helpful when you need to check if the payments work.


  Open ngrok and type
```bash
  > ngrok http 8000

  Then add the url from ngrok inside allowed host in settings.py

  Inside cart/views.py add this code

  from django.views.decorators.csrf import csrf_exempt

  add @csrf_exempt above every functions

  Then go to the url that ngrok generated for your server and test payment and django signals.
```

#### Changing the title of webpage
To change title of every page you need to go to all templates that are inside the project
and change the title inside every template. \
If you are using PyCharm click "ctrl" + "shift" + "f" and type <title>. \
That should make it a lot easier


#### Changing the content of emails

This website can send emails in a few cases:
- When user successfull create a new account
- When user is changing his password
- When user paid for a orders
- When the payment got cancelled

First you need to go to file called "accounts". Then open folder called "templates" \
and open files which are starting with "email". \
You can easely modify the content of the emails. \

Now go to file called views.py. \
Change the value of variable subject_email in line 34 and 105 \
Now open folder called "payment" and "templates" and to the same thing in this folder. \
Then open file called "views.py" and change the value of variable subject_email in line \
21 and 45.


#### Changing static files:
There is only one way to change PDF files that are included inside website. \
Go to your main folder, there is folder called "static" and inside this folder \
there is folder called "pdf". \
Inside this folder you can add your pdf files. \
Then go to application called "SHOP_INFO" in your project and folder called "templates" \
Inside this folder is a file called "all_documents.html" open it and change the file name \
that you just added.

#### For example:


```bash
  You added file called nowy_regulamin.pdf

  So you gonna change this line of code:

  (old) <a href="{% static '/pdf/regulamin.pdf' %}">Sprawdź regulamin sklepu</a>

  (new) <a href="{% static '/pdf/nowy_regulamin.pdf' %}">Sprawdź regulamin sklepu</a>
```





## API Reference

#### All available API

```http
  127.0.0.1:8000/shop_info/api
```

On this url are displayed links for all available API:
#### Only admin user can get access
- [GET] Product
- [GET] Category
- [POST] Product
- [POST] Category
- [GET] Order
- [GET] OrderItem
- [POST] Coupons
- [GET] Coupons
- [GET] Delivery
- [POST] Delivery
## License

[MIT](https://choosealicense.com/licenses/mit/)
