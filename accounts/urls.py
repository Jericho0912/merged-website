from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #ADMIN SIDE
    path('adminhome/', views.home, name="home"),
    path('logout/', views.logoutUser, name="logout"),

    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>', views.customer, name="customer"),
    path('create_list/',views.createList, name="create_list"),
    path('delete_list/<event_id>',views.deleteList, name="delete_list"),
    path('update_info/<str:pk>', views.Updateinfo, name="update_info"),
    path('delete_info/<str:pk>', views.deleteinfo, name="delete_info"),

    #CLIENT SIDE    
    path('SignUp/', views.registerPage, name="SignUp"),
    path('SignIn/', views.loginPage, name="SignIn"),
    path('', views.clientHome, name="Home"),
    # path("SignIn/", views.SignIn, name="SignIn"),
    # path("SignUp/", views.SignUp, name="SignUp"),
    path("Features_Insights/", views.Features_Insights, name="Features_Insights"),
    path("AboutUs_Contact/", views.AboutUs_Contact, name="AboutUs_Contact"),
    path("Client_Dash/", views.view_data, name="Client_Dash"),

    #CONNECTION
    # path("Data/",views.view_data, name="connection")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

