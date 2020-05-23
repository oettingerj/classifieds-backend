**Table of Contents**
[Django: The Backend Web Framework](<#django-the-backend-web-framework>)<br />
&emsp;[Organizational Hierarchy & Nomenclature](<#organizational-hierarchy-nomenclature>)<br />
&emsp;[The File Hierarchy](<#the-file-hierarchy>)<br />
&emsp;[Data Flow](<#data-flow>)<br />
&emsp;&emsp;[URL mapper](<#url-mapper>)<br />
&emsp;&emsp;[View](<#view>)<br />
&emsp;&emsp;[Model](<#model>)<br />
&emsp;&emsp;[Serializers](<#serializers>)<br />
&emsp;&emsp;[MVT Architecture](<#mvt-architecture>)<br />
	[API Endpoints](<#api-endpoints>)<br />
		[Testing](<#testing>)<br />
			[Google id_token Generation](<#google-id-token-generation>)<br />
			[Sending an HTTP Request](<#sending-an-http-request>)<br />
				[Logging in](<#logging-in>)<br />
				[GET Requests](<#get-requests>)<br />
				[POST Requests](<#post-requests>)<br />

# Django: The Backend Web Framework
## Organizational Hierarchy & Nomenclature
An instance of a collective hierarchy of files whose purpose is to instruct Django for a particular web-app is known as a project (called “classifieds_project” for this project). A project contains at least one app. An app is a collection of files that govern Django’s operation as it relates to a specific domain. The scope of such a domain is variable, and is discretionary. One may elect to consolidate all behavior to a single app, or distribute it across multiple apps. 

This particular project contains an app called “main_app” which houses nearly all of the project’s functionality. This project contains another app called “auth_app” which handles customized user authentication (verifying that a user is who they claim they are) and authorization (determining what a user has permission to do once they have been authenticated). 

Notably the Django nomenclature of an app is distinct from an app in the general term “web app.” A single web app, in which Django can act as the back end, may have many apps (in the Django sense of the word). In addition to one or more apps, a Django project always has a manage.py file, and may optionally have a database contained within the outer project directory.

## The File Hierarchy
\classifieds_project(see note 1)
	manage.py
	\classifieds_project (see note 2)
		config.py
		connect.py
		settings.py
		urls.py
		wsgi.py
	\main_app
		models.py
		views.py
		serializers.py
		admin.py
		\management
		\migrations
		\templates
		tests.py
	\auth_app
		models.py
		views.py
		custom_auth.py (see note 3)
		admin.py
		apps.py
		\management
		\migrations
		\templates
		tests.py
	db.sqlite3 (see note 4)
	
Note 1: a.k.a. the outer project directory
Note 2: a.k.a. the inner project directory (by convention, this directory has the same name as the outer project directory)
Note 3: defines the authentication backend class used by the project
Note 4: this local SQLite db is Django default when developoing locally, but in this project has since been replaced by a remote PostgreSQL db 
	


## Data Flow
### URL mapper 
(urls.py)
Django is called to action when it receives an HTTP request (from the front-end, for example). The URL mapper (urls.py) redirects the HTTP request to the appropriate view based on the request URL. Each app has its own views (views.py), so the app the request is being redirected to must be specified. Patterns of strings or digits in the URL can be matched and passed as data to a view function.

### View 
(views.py)
The view of the specified app receives the redirected HTTP request and reads/writes the necessary data via the model (models.py), which is also specific to a particular app. Although formatting information need not be returned, the view can optionally delegate formatting to an app’s templates (templates.py). Once the necessary actions, if any, have been executed upon the data the view returns an HTTP response. Note that the serializers can play a necessary intermediate role.

### Model 
(models.py)
Models are Python classes that govern the structure of an app’s data (ultimately informing necessary actions to be performed upon the database and which dictate the structure of the database itself). Typically in models.py, when a new class is defined the Model class is inherited, which provides the necessary methods to manage data (such as adding, modifying, and deleting data), and to query data. Generally, each new class defined in models.py correlates to a table in the database, and each Python class attribute correlates to an attribute in the respective database table. Deviations from this structure may be observed when considering classes that manage other classes. For example, auth_app/views.py contains a class that defines a User, and another class that governs how a normal user and a superuser should be created. This is standard practice when defining a custom users class. Note that a single database is used across all apps.

### Serializers 
(serializers.py)
Serializers provide for both serialization (transforming data such as a Django queryset or model instance to native Python data types) and deserialization (parsing data incoming data from an HTTP request, validating it, and converting it into a complex dataset that Django’s methods can act upon). Each app has its own set of serializers, which are defined as Python classes, often that inherit from the ModelSerializer class.

### MVT Architecture
Django refers to its organizational architecture as Model View Template (MVT); although it is similar to the Model View Controller (MVC) architecture, it is not synonymous. Django’s view presents the model in a particular format, just as the view in an MVC architecture does. In some ways, however, Django delegates what would be the role of the controller to the URL mapper and serializers.

## API Endpoints
### Testing
#### Google id_token Generation
Successful login with Google credentials on a client-facing web app will return a googleUser object; an id_token can be obtained from this object. Generation of the token can be completed as follows:
1. Download the directory “GoogleIDTokenGen” (located in the same directory on the shared Google Drive as this “Documentation” document)
2. On your machine, open the index.html file inside of the directory in a text editor
3. Check that the meta tag on line 5 has an attribute “content” that is set to the appropriate OAuth 2.0 Client ID as a string (the trailing portion of this string should read .apps.googleusercontent.com”. There is no need to change this attribute’s value for generic testing purposes.
4. Open a command line interface on your machine, and cd to the “GoogleIDTokenGen” directory that you downloaded
5. Start a Python web server that serves the index.html file by entering the command “python3 -m http.server 5000” (port 5000, is specified as to allow simultaneous operation of a Django server on the default port of 8000). Attempting to use this utility without accessing it from a server may be flagged by Google as a security threat and may prohibit access.
6. In a web browser, navigate to “localhost:5000”
7. Click the Google sign in button at the top of the webpage; you will be asked to choose an account/enter credentials to continue to “Carleton Classifieds.” If you are presented with any other destination this utility should be considered compromised and immediate abortion is thus advised. Note that you must use an account having a domain of carleton.edu
8. Click the “Copy id_token” button to copy the presented id_token to your clipboard. You are now in possession of a valid Google id_token that can be used to authenticate to the backend Django server.
#### Sending an HTTP Request
##### Logging in
With a valid Google id_token, authentication to the Django backend can proceed, followed by subsequent testing of other endpoints. Begin by downloading the application Insomnia Core, and proceed as follows:
1. Open Insomnia and click on “New Request”
2. Select the method “POST” 
3. Select “Form URL Encoded,” and create the request
4. By the POST method, enter the base of the url of the Django server along with the port number (running locally, this often defaults to http://127.0.0.1:8000)
5. In the “New name” field enter “idtoken” and in the “New value” field paste in the Google id_token that you copied previously
6. Specify the API endpoint you wish to access. Since you have yet to authenticate, this should be tokensignin (the url should now read http://127.0.0.1:8000/tokensignin/). Note the absence of the trailing forward slash will cause an error.
7. You should receive an HTTP_200 OK response, along with two cookies which will be used with future HTTP requests to endpoints that provide the server with your identity as a logged in user. If unsuccessful, try obtaining a new Google id_token; these generally expire after 1 hour. One cookie has the key “sessionid” and the other cookie has the key “csrftoken”

##### GET Requests
After logging-in per above, proceed as follows:
1. Use the same request that you used to login, as this will preserve the necessary cookies. Change the method of the request, however, to “GET”
2. Change the url to direct to the appropriate endpoint, ensuring the presence of the trailing forward slash as appropriate
3. Send the request

##### POST Requests
As POST requests change data in the database, it is even more critical for the authenticity of the user to be verified. In particular, Django is looking to protect against Cross-Site Request Forgery (CSRF); Django expects the POST request to contain a “csrftoken” for it to examine. This token must exist in two places within the HTTP(S) POST request; additionally, the request must contain the sessionid. Following initial authentication (see “Logging in” above), the client is given two cookies, one containing the “csrftoken” and the other the “sessionid.” Sending a subsequent POST request to another endpoint via Insomnia will automatically include those cookies in the POST request; Django also expects the POST request to have a separate header that contains the CSRF token. Proceed as follows to perform a POST request:
1. Obtain the value of the “csrftoken” by clicking “Cookie” then “Manage Cookies” in Insomnia
2. Click on edit for the cookie that begins with “csrftoken=”
3. Copy the value of the cookie in the window that appears, then close the window, and close the “Manage Cookies” window
4. Click on “Header” in Insomnia
5. Enter “X-CSRFTOKEN” where it reads “New header” and paste the csrftoken value that you previously copied in the “New value” field
6. You no longer need the “Content-Type” header as you did for initial authentication, but you may wish to keep the box checked to ease in future login activity
7. Change the url to direct to the appropriate endpoint, ensuring the presence of the trailing forward slash as appropriate
8. Send the request 
