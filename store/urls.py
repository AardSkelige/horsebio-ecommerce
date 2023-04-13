from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:product_slug>', get_category, name='view_category'),
    path('product/<slug:product_slug>', get_product, name='view_product'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]
