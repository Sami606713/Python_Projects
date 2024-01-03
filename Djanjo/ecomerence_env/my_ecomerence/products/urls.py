from django.urls import path,include
from rest_framework import routers
from products import views

# make a router 
router=routers.DefaultRouter()
router.register(r"api_products",views.ProductViewsets)
urlpatterns = [
    path("",include(router.urls)),
    path("index",views.index,name="index"),
    path("log_in",views.log_in,name="log_in"),
    path("signup",views.signup,name="signup"),
    path("contact",views.contact,name="contact"),
    path("about",views.about,name="about"),
    path("product_view/<int:id>",views.product_view,name="product_view"),
    path("shoping_cart",views.cart,name="cart"),
    path("order",views.order,name="order")
]