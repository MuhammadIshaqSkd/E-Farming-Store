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
    path('home/',views.home),
    path("productview/<int:myid>",views.productview),
    path("order/",views.order),
    path("status/",views.status),
    path("tracker/",views.tracker),
    path("forgottrackingid/",views.forgottrackingid),
    path("checkingcnicids/",views.checkingcnicids),
    path("delivers/",views.delivers),
    path("deshboard/",views.deshboard),
    path("updtecash/<int:order_id>",views.updtecash),
    path("logout/",views.logout),
    path("deletOrder/",views.deletOrder),
    path("login/",views.delivers),

    path("search/",views.search),


]