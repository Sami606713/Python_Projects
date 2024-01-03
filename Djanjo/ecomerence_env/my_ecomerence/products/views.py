from django.shortcuts import render,redirect
from django.http import HttpResponse
from products.models import Products,Contact
import math,os
# Api imports
from rest_framework import viewsets
from rest_framework import permissions
from products.models import Products
from products.serializers import ProductSerializer
# costom log-in imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Email sending
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
# Api end points class
class ProductViewsets(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # Fetch the data
    def get_data(self,id):
        try:
            return Product.object.get(pk=id)
        except:
            raise HttpResponse("<h1>Id not found</h1>")

# End of API

# products end point
def index(request):
    product=Products.objects.all()
    # Nbr od slides we want to display
    n=len(product)
    nbr_of_slides=n//4 + math.ceil((n/4)-(n//4))
    # For displaying the image

    params={"product":product,"Nbr of slides":nbr_of_slides,"range":range(nbr_of_slides)}
    return render(request,"index.html",params)


def contact(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        phone_nbr=request.POST.get("phone_number")
        email=request.POST.get("email")
        msg=request.POST.get("message")
        print(name,phone_nbr,email,msg)

        contact=Contact(name=name,email=email,phone=phone_nbr,msg=msg)
        contact.save()

        subject = 'New Contact Form Submission'
        message = f'Name: {name}\nEmail: {email}\nPhone: {phone_nbr}\nMessage: {msg}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['sami606713@gmail.com','sami606715@gmail.com']  # Add your email or a list of emails here

        send_mail(subject, message, from_email, recipient_list,fail_silently=False,)
    return render(request,"contact.html")


def about(request):
    # return HttpResponse("<h1>About</h1>")
    return render(request,"about.html")

def signup(request):
    if(request.method=="POST"):
        user_name=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        # confirm_pass=request.POST.get("pass")

        new_user=User.objects.create_user(user_name,email,password)
        new_user.save()
        return redirect("log_in")
    return render(request,"registration/signup2.html")


def log_in(request):
    if (request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)
        # print(user)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return redirect("/product/log_in")
    return render(request,"registration/log_in.html")

# Product view
def product_view(request,id):
    # fetch the item
    product=Products.objects.filter(pk=id)
    return render(request,"product_view.html",{"fetch_product":product[0]})

# Cart 
def cart(request):
    return render(request, "shoping_cart.html")

# order 
def order(request):
    if(request.method=="post" and user.is_authenticated):
        name=request.POST.get("name")
        phone_nbr=request.POST.get("nbr")
        address=request.POST.get("addr")
        email=request.POST.get("email")
        province=request.POST.get("province")
        city=request.POST.get("city")
        area=request.POST.get("area")
        print(name,phone_nbr,address,email,province,city,area)
    return render(request,"order.html")
# end order