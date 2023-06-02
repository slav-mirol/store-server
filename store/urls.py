"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import include

from store.products import views
from store.users import views as views_users
from store.orders import views as views_orders

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='home'),
    path('create-products', views.CreateProductAPIView.as_view()),
    path('create-categories', views.CreateProductCategoryAPIView.as_view()),
    path('get-products', views.ShowAllProducts.as_view()),
    path('get-categories', views.ShowAllCategories.as_view()),
    path('user/create', views_users.CreateUserAPIView.as_view()),
    path('user/update', views_users.UserRetrieveUpdateAPIView.as_view()),
    path('user/auth', views_users.authenticate_user),
    path('filter-products/category', views.ShowProductsFromCategory.as_view()),
    path('orders/create-cart', views_orders.CreateCart.as_view()),
    path('orders/create-order', views_orders.CreateOrder.as_view()),
    path('cart/get-cart/<int:user>', views_orders.GetUsersCart.as_view()),
    path('orders/get-orders/<int:user>', views_orders.GetUsersOrders.as_view()),
]
