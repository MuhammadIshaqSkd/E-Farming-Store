"""asc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('homev/',views.homev),

    path('vehicles/',views.vehicles),
    path('tools/',views.tools),
    path('drones/',views.drones),

    path("productviewV/<int:myid>",views.productviewV),
    path("productviewT/<int:myid>",views.productviewT),
    path("productviewD/<int:myid>",views.productviewD),

    path("bookingV/<int:myid>",views.bookingV),
    path("bookingT/<int:myid>",views.bookingT),
    path("bookingD/<int:myid>",views.bookingT),

    path("bookingOrder/",views.bookingOrder),

    path("search/",views.search),

    path("branches/",views.branches),
    path("branchesK/",views.branchesK),
    path("branchesR/",views.branchesR),
    path("branchesL/",views.branchesL),
    path("branchesC/",views.branchesC),


    path("complaints/",views.complaints),
    path("bookingStatus/",views.bookingStatus),
    path("checkingbookingStatus/",views.checkingbookingStatus),
    path("cancelbooking/",views.cancelbooking),


    path("contactus/",views.contactus),


]