These are the endpoints that can be used (by frontend code or for testing) to access the database.

Authentication:
login (POST):   tokensignin/
logout (POST, GET): logout/

Ride Listings:
create (POST):  rideposting/create/
edit (POST):    rideposting/edit/<pk>/<created>/<datetime>/<startLocation>/<endLocation>/<passengers>/<distance>/<sold>/
delete (POST):  rideposting/delete/<pk>/
toggle sold (POST): rideposting/changesold/<pk>/<new_sold>/
view details (GET): rideposting/view/postingdetails/<pk>/
mark liked (POST):  rideposting/like/<pk>/
mark unliked (POST):    rideposting/unlike/<pk>/
view liked (GET):   rideposting/displayliked/
    
Item Listings:
create (POST):  itemposting/create/
edit (POST):    itemposting/edit/<pk>/<created>/<title>/<description>/<user>/<img>/<price>/<sold>/
delete (POST):  itemposting/delete/<pk>/
toggle sold (POST): itemposting/changesold/<pk>/<new_sold>/
view details (GET): itemposting/view/postingdetails/<pk>/
mark liked (POST):  itemposting/like/<pk>/
mark unliked (POST):    itemposting/unlike/<pk>/
view liked (GET):   itemposting/displayliked/
    
Navigation:
view all listings (GET):  api/get/available_postings//
view listings by category (GET):  api/get/available_postings/<category>/
view all rides (GET): api/get/available_rides/
view own listings (GET):  api/get/own_postings/
search listings (GET):    api/search/<keyword>/
