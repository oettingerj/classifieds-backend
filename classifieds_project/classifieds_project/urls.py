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
    path('test01/', views.test01),
    path('test02/', views.test02),
#    path('api/create/posting/<user_pk>/<timePosted>/<category>/<prospective>/<fulfilled>/<description>/<audience>/', views.create_posting),
    path('rideposting/create/<created>/<user>/<datetime>/<startLocation>/<endLocation>/<passengers>/<distance>/', views.create_ridelisting),
    path('itemposting/create/<created>/<title>/<description>/<user>/<img>/<price>/<sold>/', views.create_itemlisting),
    path('rideposting/edit/<created>/<user>/<datetime>/<startLocation>/<endLocation>/<passengers>/<distance>/', views.edit_ridelisting),
    path('itemposting/edit/<created>/<title>/<description>/<user>/<img>/<price>/<sold>/', views.edit_itemlisting),
    path('rideposting/delete/<pk>/', views.delete_ridelisting),
    path('itemposting/delete/<pk>/', views.delete_itemlisting),
    url(r'api/get/available_postings/(?P<category>\w+|)/', views.get_available_postings),
    url(r'api/get/own_postings/', views.get_own_postings),
    path('accounts/', include('allauth.urls')), 
    path('api/search/<keyword>/', views.search_postings),
    path('rideposting/togglesold/<pk>/', views.toggle_ridelisting_sold),
    path('itemposting/togglesold/<pk>/', views.toggle_itemlisting_sold),
    path('rideposting/view/postingdetails/<pk>/', views.view_ridelisting_details),
    path('itemposting/view/postingdetails/<pk>/', views.view_itemlisting_details),
    path('rideposting/save/<user_pk>/<pk>/', views.save_ridelisting),
    path('itemposting/save/<user_pk>/<pk>/', views.save_itemlisting),
    path('rideposting/unsave/<user_pk>/<pk>/', views.unsave_ridelisting),
    path('itemposting/unsave/<user_pk>/<pk>/', views.unsave_itemlisting),
    path('rideposting/displaysaved/<user_pk>/<pk>/', views.display_saved_ridelistings),
    path('itemposting/displaysaved/<user_pk>/<pk>/', views.display_saved_itemlistings)
]
