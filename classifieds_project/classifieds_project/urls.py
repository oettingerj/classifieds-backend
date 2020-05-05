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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('tokensignin/', auth_views.authenticate),
    path('logout/', auth_views.logout),
    path('api/create/posting/<user_pk>/<timePosted>/<category>/<prospective>/<fulfilled>/<description>/<audience>/', views.create_posting),
    path('rideposting/create/<posting_pk>/<dateTimeOfRide>/<startLocation>/<endLocation>/<numberOfPeople>/<willingToPay>/<payment>/',views.create_rideposting),
    path('api/create/itemPosting/<posting_pk>/<images>/<price>/<forSale>/<forLoan>', views.create_itemposting),
    path('rideposting/edit/<ride_pk>/<posting_pk>/<dateTimeOfRide>/<startLocation>/<endLocation>/<numberOfPeople>/<willingToPay>/<payment>/', views.edit_rideposting),
    path('itemposting/edit/<posting_pk>/<images>/<price>/<forSale>/<forLoan>', views.edit_itemposting),
    path('rideposting/delete/<key>/', views.delete_rideposting),
    path('itemposting/delete/<item_pk>/', views.delete_itemposting),
#    path('api/list/posting/', views.posting_list),
    url(r'api/get/available_postings/(?P<category>\w+|)/', views.get_available_postings),
    url(r'api/get/postings_by_id/(?P<user_id_num>[0-9]+)/', views.get_postings_by_id),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="sample/index.html")), 
    path('api/search/<keyword>/', views.search_postings),
    path('api/toggle/fulfilled/<pk>/', views.toggle_posting_fulfilled),
    path('api/view/posting_details/<pk>/', views.view_posting_details),
    path('api/saved/saveposting/<posting_pk>/<user_pk>/', views.save_posting),
    path('api/saved/unsaveposting/<posting_pk>/<user_pk>/', views.unsave_posting),
    path('api/saved/displaypostings/<user_pk>/', views.display_saved_postings)
]
