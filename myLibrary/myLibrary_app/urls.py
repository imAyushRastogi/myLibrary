"""
URL configuration for myLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('', home),
    path('home', home),
    path('shop', shopping),
    path('save', save_stud),
    path('books', books),
    path('readers',readers),
    path('readers/add', save_reader),
    path('readers/delete', delete_reader),
    path('books/add',save_book ),
    path('books/delete', delete_book ),
    path('mybag', mybag ),
    path('return', returns ),
]
