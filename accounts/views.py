from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
import pytz
from datetime import time , date
from .models import *
from .forms import addlist , updateinfo ,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login as django_login

import serial

#connection esp32
def connection(request):
    ser=serial.Serial("COM3",115200)
    data=ser.readline().decode().strip()
    ser.close()

    context = {
        "data" : data
    }

    return render(request, "my_thessis/conn.html", context)

# django_login(request, user)
# Create your views here.

#ADMIN SIDE

@login_required(login_url='login')
def home(request):
    customers = userinfo.objects.all()
    total_users = userinfo.objects.count()
    #time
    now = timezone.now().astimezone(pytz.timezone('Asia/Manila'))
    now_non_military = time(hour=now.hour , minute=now.minute, second=now.second)
    now_formatted = now_non_military.strftime('%I:%M %p')

    #date
    today = date.today()
    today_formatted = today.strftime('%Y-%m-%d')

    #Products
    products = Product.objects.all()
    total_products = products.count()
    
    #dictionary
    context = {
        'customers': customers,
        'total_users': total_users,
        'now' : now,
        'now_formatted': now_formatted,
        'today_formatted': today_formatted,
        'total_products': total_products,
        
               }

    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products, })

@login_required(login_url='login')
def customer(request, pk_test):
    customer = userinfo.objects.get(id=pk_test)
    context = { 'customer': customer}
    return request(request, 'accounts/customer.html', context)

@login_required(login_url='login')
def createList(request):
    form = addlist()
    if request.method == 'POST':
      #print('Printing POST:',request.POST)
      form = addlist(request.POST)
      if form.is_valid():
          form.save()
          return redirect('products') #for sending to product page


    context = {'forms': form,}
    return render(request,'accounts/list_form.html', context)

@login_required(login_url='login')
def Updateinfo(request, pk):
   info = userinfo.objects.get(id=pk)
   form = updateinfo(instance=info)

   if request.method == 'POST':
      #print('Printing POST:',request.POST)
      form = updateinfo(request.POST,instance=info)
      if form.is_valid():
          form.save()
          return HttpResponseRedirect("/") #for sending to product page
             

   context = {'form': form ,}
   return render(request, 'accounts/update.html', context)

@login_required(login_url='login')
def deleteinfo(request, pk):
  info = userinfo.objects.get(id=pk)
  if request.method == "POST":
    info.delete()
    return redirect('/')
  context={'info':info}
  return render(request, 'accounts/delete.html', context)
  
# def deleteList(request, pk):
#   info = Product.objects.get(name=pk)
#   if request.method == "POST":
#     info.delete()
#     return redirect('/')
#   context={'info':info}
#   return render(request, 'accounts/delete.html', context)

# def deleteList(request ,event_id):
#     event = Product.objects.get(pk = event_id) # plss can u fckingg remember that this event id is import for querying data 
#     event.delete()
#     return redirect('products')

#     context = {'forms': form,}
#     return render(request,'accounts/list_form.html', context)
@login_required(login_url='login')
def deleteList(request, event_id):
  info = Product.objects.get(pk = event_id)
  if request.method == "POST":
    info.delete()
    return redirect('products')
  context={'info':info}
  return render(request, 'accounts/deleteprod.html', context)
  

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('user')
            messages.success(request,'Account was Created for ' + user)
            return redirect('SignIn')
            
    context = {'form':form}
    return render(request, 'my_thesis/SignUp.html', context)

def loginPage(request): 
    
    if request.method == 'POST':
       username=request.POST.get('username')
       password=request.POST.get('password')

       user = authenticate(request, username=username, password=password)
       
       if user is not None:
          login(request, user)
          return redirect('Client_Dash')
       else:
          messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'my_thesis/SignIn.html', context)

@login_required(login_url='login')
def logoutUser(request):
   logout(request)
   return redirect('login')




#CLIENT SIDE


# @login_required(login_url='SignIn')
def clientHome(request):
    return render(request, "my_thesis/Home.html")

# @login_required(login_url='SignIn')
# def SignIn(request): 
    
#     if request.method == 'POST':
#        username=request.POST.get('username')
#        password=request.POST.get('password')

#        user = authenticate(request, username=username, password=password)
       
#        if user is not None:
#           login(request, user)
#           return redirect('Client_Dash')
#        else:
#           messages.info(request, 'username OR password is incorrect')

#     context = {}
#     return render(request, 'my_thesis/SignIn.html', context)

    
#     # return render(request,"my_thesis/SignIn.html")

# def SignUp(request):
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request,'Account was Created for ' + user)
#             return redirect('SignUp')
            
#     context = {'form':form}
#     return render(request, 'my_thesis/SignUp.html', context)



def Features_Insights(request):
    return render(request, "my_thesis/Features_Insights.html")

def AboutUs_Contact(request):
    return render(request, "my_thesis/AboutUs_Contact.html")

@login_required(login_url='SignIn')
def Client_Dash(request):
    return render(request, "my_thesis/Client_Dash.html")

# @login_required(login_url='SignIn')
def logoutUser(request):
   logout(request)
   return redirect('Home')


def login_histories(request):

    if not request.user.is_authenticated:
        return HttpResponse("<h1>Please login to see your login histories</h1>")\
        
    active_logins = request.user.active_logins

    active_logins_html = ""
    for login in active_logins:
        active_logins_html += f'<li>{login.ip} - {login.date_time} - {login.user_agent}</li>'

    return HttpResponse(
    f"""
        <h1>Active Logins</h1>
        <ul>
            {active_logins_html}
        </ul>
    """
    )

def today(request):
    """Shows todays current time and date."""
    today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    context = {'today': today}
    return render(request, context)