"""classifieds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from main_app import views
from auth_app import views as auth_views
from django.conf.urls import url
from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('tokensignin/', auth_views.authenticate),
    path('logout/', auth_views.logout),
    path('rideposting/create/', views.create_ridelisting),
    path('itemposting/create/', views.create_itemlisting),
    path('rideposting/edit/<pk>/<created>/<datetime>/<startLocation>/<endLocation>/<passengers>/<distance>/<sold>/', views.edit_ridelisting),
    path('itemposting/edit/<pk>/<created>/<title>/<description>/<user>/<img>/<price>/<sold>/', views.edit_itemlisting),
    path('rideposting/delete/<pk>/', views.delete_ridelisting),
    path('itemposting/delete/<pk>/', views.delete_itemlisting),
    url(r'api/get/available_postings/(?P<category>[\w|\s]*)/', views.get_available_postings),
    url(r'api/get/own_postings/', views.get_own_postings),
    url('api/get/available_rides/', views.get_available_rides),
    path('api/search/<keyword>/', views.search_postings),
    path('rideposting/changesold/<pk>/<new_sold>/', views.change_ridelisting_sold),
    path('itemposting/changesold/<pk>/<new_sold>/', views.change_itemlisting_sold),
    path('rideposting/view/postingdetails/<pk>/', views.view_ridelisting_details),
    path('itemposting/view/postingdetails/<pk>/', views.view_itemlisting_details),
    path('rideposting/like/<pk>/', views.like_ridelisting),
    path('itemposting/like/<pk>/', views.like_itemlisting),
    path('rideposting/unlike/<pk>/', views.unlike_ridelisting),
    path('itemposting/unlike/<pk>/', views.unlike_itemlisting),
    path('rideposting/displayliked/', views.display_liked_ridelistings),
    path('itemposting/displayliked/', views.display_liked_itemlistings)
]
