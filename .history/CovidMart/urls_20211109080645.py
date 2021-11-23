from django.urls import path
from . import views

urlpatterns = [
   path('', views.home_view, name='home'),
   path('login', views.login_view, name='login'),
   path('cart', views.cart_view, name='cart'),
   path('produce', views.produce_view, name='produce')
]