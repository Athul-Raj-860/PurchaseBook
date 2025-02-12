"""
URL configuration for Purchase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Book import views


urlpatterns = [ path('admin/', admin.site.urls),
                path('',views.Login,name='Login'),
                path('Home/',views.Home,name='Home'),
                path('Sign_Up/',views.Sign_Up,name='Sign_Up'),
                path('Forgot/',views.Forgot,name='Forgot'),
                path('Update_User/<int:id>/',views.Update_User,name='Update_User'),
                path('Logout/',views.Logout,name='Logout'),
                path('Add_Wishlist/<int:id>/', views.Add_Wishlist, name='Add_Wishlist'),
                path('View_Wishlist/', views.View_Wishlist, name='View_Wishlist'),
                path('Remove_Wishlist/<int:id>/', views.Remove_Wishlist, name='Remove_Wishlist'),
                path('Add_Book/',views.Add_Book,name='Add_Book'),
                path('more info/<int:id>/', views.Book_Details, name='Book_Details'),
                path('Add_Cart/<int:id>/', views.Add_Cart, name='Add_Cart'),
                path('View_Cart/', views.View_Cart, name='View_Cart'),
                path('Remove_Cart/<int:id>/', views.Remove_Cart, name='Remove_Cart'),
                path('Update_Book/<int:id>/', views.Update_Book, name='Update_Book'),
                path('Delete_Book/<int:id>/', views.Delete_Book, name='Delete_Book'),
                path('Ordered/',views.View_Order,name='Ordered Book'),
                path('Book_Payment/<int:id>', views.Book_Payment, name='Book_Payment'),
                path('Merchant/',views.Merchant,name='Merchant'),
                path('Go_Back',views.Go_Back,name='Go_Back')
                ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
