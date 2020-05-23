# API Endpoints
These are the endpoints that can be used (by frontend code or for testing) to access the database. Instructions on how to use these endpoints can be found in the README.md file.

## Authentication:
&emsp;login (POST):   tokensignin/<br />
&emsp;logout (POST, GET): logout/

## Ride Listings:
&emsp;create (POST):  rideposting/create/<br />
&emsp;edit (POST):    rideposting/edit/\<pk>/\<created>/\<datetime>/\<startLocation>/\<endLocation>/\<passengers>/\<distance>/\<sold>/<br />
&emsp;delete (POST):  rideposting/delete/\<pk>/<br />
&emsp;toggle sold (POST): rideposting/changesold/\<pk>/\<new_sold>/<br />
&emsp;view details (GET): rideposting/view/postingdetails/\<pk>/<br />
&emsp;mark liked (POST):  rideposting/like/\<pk>/<br />
&emsp;mark unliked (POST):    rideposting/unlike/\<pk>/<br />
&emsp;view liked (GET):   rideposting/displayliked/
    
## Item Listings:
&emsp;create (POST):  itemposting/create/<br />
&emsp;edit (POST):    itemposting/edit/\<pk>/\<created>/\<title>/\<description>/\<user>/\<img>/\<price>/\<sold>/<br />
&emsp;delete (POST):  itemposting/delete/\<pk>/<br />
&emsp;toggle sold (POST): itemposting/changesold/\<pk>/\<new_sold>/<br />
&emsp;view details (GET): itemposting/view/postingdetails/\<pk>/<br />
&emsp;mark liked (POST):  itemposting/like/\<pk>/<br />
&emsp;mark unliked (POST):    itemposting/unlike/\<pk>/<br />
&emsp;view liked (GET):   itemposting/displayliked/
    
## Navigation:
&emsp;view all listings (GET):  api/get/available_postings//<br />
&emsp;view listings by category (GET):  api/get/available_postings/\<category>/<br />
&emsp;view all rides (GET): api/get/available_rides/<br />
&emsp;view own listings (GET):  api/get/own_postings/<br />
&emsp;search listings (GET):    api/search/\<keyword>/
