from .models import *
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.views.generic.detail import DetailView
from django.views.generic import ListView, DetailView
from.models import  Listing
def home(request):
    return render(request, 'user/home.html')

def register(request):
    if request.method == 'POST':
        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email is already been used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username,password=password,email=email,
                                                    first_name=first_name,last_name=last_name)
                    # Login after Register
                    auth.login(request,user)
                    messages.success(request,'You are now logged in')
                    return redirect('/login')
                    #user.save()
                    #messages.success(request,'Successfully Registered, You can now log in')
                    #return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'user/register.html')



def user_login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('/dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def dashboard(request):
    # user_contacts =Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    # context={
    # 'contacts':user_contacts
    # }
    return render(request, 'user/dashboard.html')  # ,context)



def logout_request(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('/')


def about(request):
    #Get all realtors
    #realtors =Realtor.objects.order_by('-hire_date')

    #Get MVP
    #mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    #context ={
        #'realtors': realtors,
        #'mvp_realtors': mvp_realtors
    #}
    return render(request,'user/about.html')#context)

def index(request):
    #listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    #paginator = Paginator(listings,3)
    #page = request.GET.get('page')
    #paged_listings =paginator.get_page(page)

    #context ={
        #'listings': paged_listings
    #}
    return render(request,'user/index.html')#,context)

def listings(request):
    listings = Listing.objects.all()
    return render(request=request, template_name='user/listings.html', context={'listings':listings})



def detail(request,pk):
    listing = get_object_or_404(Listing, pk=pk)
    context ={'listing':listing}
    return render(request,'user/detail.html', context)








def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    #Province
    if 'province' in request.GET:
        province = request.GET['province']
        if province:
            queryset_list = queryset_list.filter(province__iexact=province)
    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)
    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context ={
        'price_choices':price_choices,
        'bedroom_choices': bedroom_choices,
        'province_choices':province_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request,'user/search.html',context)
