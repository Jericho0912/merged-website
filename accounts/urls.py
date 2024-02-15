from django.urls import path
from . import views

urlpatterns = [
    
    #ADMIN SIDE
    path('adminhome/', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>', views.customer, name="customer"),
    path('create_list/',views.createList, name="create_list"),
    path('delete_list/<event_id>',views.deleteList, name="delete_list"),
    path('update_info/<str:pk>', views.Updateinfo, name="update_info"),
    path('delete_info/<str:pk>', views.deleteinfo, name="delete_info"),

   

    #CLIENT SIDE    

    path('', views.clientHome, name="Home"),
    path("SignIn/", views.SignIn, name="SignIn"),
    path("SignUp/", views.SignUp, name="SignUp"),
    path("Features_Insights/", views.Features_Insights, name="Features_Insights"),
    path("AboutUs_Contact/", views.AboutUs_Contact, name="AboutUs_Contact"),
    path("Client_Dash/", views.Client_Dash, name="Client_Dash"),
]
