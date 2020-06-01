**Table of Contents**<br />
[Django: The Backend Web Framework](<#django-the-backend-web-framework>)<br />
&emsp;[Organizational Hierarchy & Nomenclature](<#organizational-hierarchy--nomenclature>)<br />
&emsp;[The File Hierarchy](<#the-file-hierarchy>)<br />
&emsp;[Data Flow](<#data-flow>)<br />
&emsp;&emsp;[URL mapper](<#url-mapper>)<br />
&emsp;&emsp;[View](<#view>)<br />
&emsp;&emsp;[Model](<#model>)<br />
&emsp;&emsp;[Serializers](<#serializers>)<br />
&emsp;&emsp;[MVT Architecture](<#mvt-architecture>)<br />
&emsp;[API Endpoints](<#api-endpoints>)<br />
&emsp;&emsp;[Testing](<#testing>)<br />
&emsp;&emsp;&emsp;[Google id_token Generation](<#google-id_token-generation>)<br />
&emsp;&emsp;&emsp;[Sending an HTTP Request](<#sending-an-http-request>)<br />
&emsp;&emsp;&emsp;&emsp;[Logging in](<#logging-in>)<br />
&emsp;&emsp;&emsp;&emsp;[GET Requests](<#get-requests>)<br />
&emsp;&emsp;&emsp;&emsp;[POST Requests](<#post-requests>)<br />
&emsp;[Running the Server](<#running-the-server>)<br />
&emsp;&emsp;[Installing Dependencies](<#installing-dependencies>)<br />
&emsp;&emsp;[Starting the Server](<#starting-the-server>)<br />
[References](<#references>)<br />

# Django: The Backend Web Framework
## Environnment Setup
These setup instructions assume that you are working in a linux-based environment (namely, the macOS operating system, Windows Subsystem for Linux in a Windows operating system, or a distro of the Linux operating system itself). Windows users are advised to install [Windows Subsystem for Linux](<https://docs.microsoft.com/en-us/windows/wsl/install-win10>). Readers are advised to sequentially follow the instructions in this "Environment Setup" section, skipping any steps that have already been performed.
### Core Tools
Fundamental tools such as git are required for the operation of this repo. Users of macOS can install the Xcode command line tools; users of other operating systems are encouraged to install git using a method of their choice, and install any other programs as instructed by the command line interface.
#### Installing the Xcode Command Line Tools (macOS only)
1. Open the application "Terminal"
2. Enter the command `xcode-select --install`


## Organizational Hierarchy & Nomenclature
An instance of a collective hierarchy of files whose purpose is to instruct Django for a particular web-app is known as a project (called “classifieds_project” for this project). A project contains at least one app. An app is a collection of files that govern Django’s operation as it relates to a specific domain. The scope of such a domain is variable, and is discretionary. One may elect to consolidate all behavior to a single app, or distribute it across multiple apps. 

This particular project contains an app called “main_app” which houses nearly all of the project’s functionality. This project contains another app called “auth_app” which handles customized user authentication (verifying that a user is who they claim they are) and authorization (determining what a user has permission to do once they have been authenticated). 

Notably the Django nomenclature of an app is distinct from an app in the general term “web app.” A single web app, in which Django can act as the back end, may have many apps (in the Django sense of the word). In addition to one or more apps, a Django project always has a manage.py file, and may optionally have a database contained within the outer project directory.

## The File Hierarchy
\classifieds_project (see note 1)<br />
&emsp;manage.py<br />
&emsp;\classifieds_project (see note 2)<br />
&emsp;&emsp;config.py<br />
&emsp;&emsp;connect.py<br />
&emsp;&emsp;\resources<br />
&emsp;&emsp;&emsp;\google_id_token_gen<br />
&emsp;&emsp;&emsp;&emsp;index.html<br />
&emsp;&emsp;settings.py<br />
&emsp;&emsp;urls.py<br />
&emsp;&emsp;wsgi.py<br />
&emsp;\main_app<br />
&emsp;&emsp;models.py<br />
&emsp;&emsp;views.py<br />
&emsp;&emsp;serializers.py<br />
&emsp;&emsp;admin.py<br />
&emsp;&emsp;\management<br />
&emsp;&emsp;\migrations<br />
&emsp;&emsp;\templates<br />
&emsp;&emsp;tests.py<br />
&emsp;\auth_app<br />
&emsp;&emsp;models.py<br />
&emsp;&emsp;views.py<br />
&emsp;&emsp;custom_auth.py (see note 3)<br />
&emsp;&emsp;admin.py<br />
&emsp;&emsp;apps.py<br />
&emsp;&emsp;\management<br />
&emsp;&emsp;\migrations<br />
&emsp;&emsp;\templates<br />
&emsp;&emsp;tests.py<br />
&emsp;db.sqlite3 (see note 4)<br />
Pipfile<br />
README.md (this file)<br />
api-endpoints.md (see note 5) <br />
	
Note 1: a.k.a. the outer project directory<br />
Note 2: a.k.a. the inner project directory (by convention, this directory has the same name as the outer project directory)<br />
Note 3: defines the authentication backend class used by the project<br />
Note 4: this local SQLite db is Django default when developoing locally, but in this project has since been replaced by a remote PostgreSQL db<br />
Note 5: this file serves as detailed documentation for the API endpoints<br />
	


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
For a listing of the API endpoints, please refer to the api-endpoints.md file contained in the root directory of this repo.
### Testing
#### Google id_token Generation
Successful login with Google credentials on a client-facing web app will return a googleUser object; an id_token can be obtained from this object. Generation of the token can be completed as follows:
1. Navigate to classifieds_project/classifieds_project/resources/google_id_token_gen in the repo
2. On your machine, open the index.html file inside of the google_id_token_gen directory in a text editor
3. Check that the meta tag on line 5 has an attribute “content” that is set to the appropriate OAuth 2.0 Client ID as a string (the trailing portion of this string should read .apps.googleusercontent.com”. There is no need to change this attribute’s value for generic testing purposes.
4. Open a command line interface on your machine, and cd to the "google_id_token_gen" directory as previously specified
5. Start a Python web server that serves the index.html file by entering the command “python3 -m http.server 5000” (port 5000, is specified as to allow simultaneous operation of a Django server on the default port of 8000). Attempting to use this utility without accessing it from a server may be flagged by Google as a security threat and may prohibit access.
6. In a web browser, navigate to “localhost:5000”
7. Click the Google sign in button at the top of the webpage; you will be asked to choose an account/enter credentials to continue to “Carleton Classifieds.” If you are presented with any other destination this utility should be considered compromised and immediate abortion is thus advised. Note that you must use an account having a domain of carleton.edu
8. Click the “Copy id_token” button to copy the presented id_token to your clipboard. You are now in possession of a valid Google id_token that can be used to authenticate to the backend Django server.
#### Sending an HTTP Request
##### Logging in
With a valid Google id_token, authentication to the Django backend can proceed, followed by subsequent testing of other endpoints. Begin by downloading the application [Insomnia Core](<https://insomnia.rest/download/>), and proceed as follows:
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

## Running the Server

### Installing Dependencies
The dependencies are delinitated in the Pipfile (contained in the root directory of this repo), and they can be installed using pipenv.

### Starting the Server
The server can be started from a local machine as follows:
1. cd to classifieds_project (the outer project directory)
2. run the command "python3 manage.py runserver"

# References
In the construction of this README.md file and development of this repository, the following sources were consulted:
- [Django documentation: general (Django Software Foundation)](https://docs.djangoproject.com/en/3.0/)
- [Django documentation: customizing authentication (Django Software Foundation)](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/)
- [Django overview (Mozilla Corporation)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
- [Django REST framework: serialization (Encode OSS Ltd.)](<https://www.django-rest-framework.org/api-guide/serializers/>)
- [Googe auth with backend server (Google LLC)](<https://developers.google.com/identity/sign-in/web/backend-auth>)
