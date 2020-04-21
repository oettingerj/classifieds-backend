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
from sample import views
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api/import/user/<name>/<email>/<role>/', views.import_user),
    path('api/import/posting/<user_pk>/<timePosted>/<category>/<prospective>/<fulfilled>/<description>/<audience>/', views.import_posting),
    path('api/import/itemposting/<posting_pk>/<images>/<price>/<forSale>/<forLoan>', views.import_itemposting),
    path('api/list/posting/', views.posting_list),
    url(r'api/get/available_postings/(?P<category>\w+|)/', views.get_available_postings),
    url(r'api/get/postings_by_id/(?P<user_id_num>[0-9]+)/', views.get_postings_by_id),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="sample/index.html")),
    path('rideposting/create/<posting_pk>/<dateTimeOfRide>/<startLocation>/<endLocation>/<numberOfPeople>/<willingToPay>/<payment>/', views.create_rideposting),
    path('rideposting/edit/<key>/<startLocation>/', views.edit_rideposting),
    path('rideposting/delete/<key>/', views.delete_rideposting),
    path('api/import/itemposting/<posting_pk>/<images>/<price>/<forSale>/<forLoan>', views.import_itemPosting),
    path('api/deleteItemPosting/<item_pk>/', views.deleteItemPosting),
    path('api/searchPostings/<keyword>/', views.searchPostings),
    path('api/postingFulfilledToggle/<pk>/', views.postingFulfilledToggle),
    path('api/viewDetails/<pk>/', views.viewDetails)
]
