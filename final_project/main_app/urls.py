from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('category/', views.category, name='category'),
    path('contact/', views.contact, name='contact'),
    path('create_account/', views.redirect_to_registration, name='create_account'),
    path('login/', views.redirect_to_login, name='login'),
    path('order_info/', views.order_info, name='order_info'),
    path('products_page/', views.products_page, name='products_page'),
    path('products_page_notepade/', views.products_page_notepade, name='products_page_notepade'),
    path('products_page_pc/', views.products_page_pc, name='products_page_pc'),
    path('products_page_redmi/', views.products_page_redmi, name='products_page_redmi'),
    path('products_page_monitor/', views.products_page_monitor, name='products_page_monitor'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('text_page/', views.text_page, name='text_page'),

]
