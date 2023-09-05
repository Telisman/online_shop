# Online Shop Project

This project is aimed at creating an Online Shop application with various functionalities, both required and optional. You can choose to develop this as a web app, a backend service (REST API), or a mobile app. The project is based on a provided dataset of products with categories and prices.

## Functionalities

### Required Functionalities

1. Product Listing Page: Display a page with all products listed.
1. Product Details Page: Provide a page where users can view the details of a specific product.
1. Shopping Cart: Implement the ability to add and remove products from the shopping cart.

### Bonus Functionalities (Optional)

1. Category Filtering: Allow users to filter products by category.
1. Product Search: Implement a search feature that allows users to search for products by name or description.
1. Sorting: Provide options for users to sort products by price in ascending or descending order

## Requirements
1. You must develop an application for at least one platform: Web, Mobile, or Backend.
1. You must use the provided dataset (https://30hills.com/api/products.json).
1. Share a link to your code repository (GitHub, Bitbucket, GitLab, etc.).





## About our app:

### Web app
This app is created in the Django framework using MongoDB as our main database.
The purpose of the application is to display data from the given link. The first view contains all products, while the second view should only contain data from a specific product.
The third operation aims to insert the desired product into the basket, as well as remove the desired product from the basket.As an additional option, a search filter by category, name and ascending or descending price has been inserted

###  Backend service (REST API)
For our Backend service (REST API) I used the Django REST framework. To create an endpoint for our API services.
List of endpoints:
```
Endpoints
Below are the endpoints available in the project:

Product Endpoints:
List Products: Get a list of all products. (API)
Endpoint: /api/products/
View: ProductList
Name: product-list

Product Detail: Get details of a specific product by ID. (API)
Endpoint: /api/products/<str:pk>/
View: ProductDetail
Name: product-detail


Shopping Cart Endpoints:
View Cart: Display the contents of the shopping cart. (API)
Endpoint: /api/cart/
View: CartView
Name: cart_view

Add to Cart: Add a product to the shopping cart by product ID. (API)
Endpoint: /api/cart/add/<str:product_id>/
View: AddToCartView
Name: add_to_cart

Remove from Cart: Remove a product from the shopping cart by product ID. (API)
Endpoint: /api/cart/remove/<str:product_id>/
View: RemoveFromCartView
Name: remove_from_cart
```




## Installation 
Step 1:
Clone file from GitHub
``` 
https://github.com/Telisman/online_shop.git
```
Step 2:
Activate virtual environment:
```
path\to\venv\Scripts\activate
```

Step 3:
Install requirements.txt file. Using terminal: 
```
pip install -r requirements.txt
``` 

Step 4:
Set up MongoDB.
The database name needs to be: online_shop_products.
settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'online_shop_products',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}
```
Step 5:
Run migrations into are terminal:
```
py manage.py makemigrations
py manage.py migrate 
```
Step 6:
Run script import_products.py in terminal to collect data from:https://30hills.com/api/products.json
```
py import_products
```
Step 7:
Run Django:
```
py manage.py runserver
```

