**NOTICE**<br />
Former versions of this repository contained passwords and usernames stored in plaintext (in this file, and in settings.py) and therefore unless such revision history has been deleted or obscured to prevent the recovery of such secure information, or unless all such usernames and passwords have since been invalidated, **THIS REPOSITORY SHOULD NOT BE MADE PUBLIC**.

Since version 1.0.1 of this repo, and version 1.1.1 of this file, such usernames and passwords exist only as references. The values for such entities are contained in a document entitled `CarletonClassifiedsCredentials.txt`. Requests to access this document should be made to Professor Sneha Narayan. Note that upon substitution of these references for their actual values in `settings.py`, subsequent pushing of this repository would compromise the security afforded by this new apparatus. Is is therefore advised that `settings.py` be included in the `.gitignore` file for this repository once all group members have cloned the repository (as of version 1.0.1 of this repo it is not included), or that an encryption tactic is employed.

This README.md file (generally) follows the [CommonMark](<https://commonmark.org>) specification of Markdown, and is best read on Github or with any application that can properly render a Markdown file.<br />

**About**<br />
Last updated (this file): 6/9/2020<br />
Version (of repo): 1.0.1<br />
Version (of this file): 1.1.2 <br />
Content: This repository contains the code for the backend of the Carleton Classified web-app. This backend is constructed using the web framework Django.<br />
Authors: Danielle Eisen '20, Sophia Maymudes '20, and John Mullan '20<br />
Mentors: special thanks to Sneha Narayan for her guidance and mentorship throughout this project, and to Mike Tie for providing his technical expertise.

**Table of Contents**<br />
[**Django: The Backend Web Framework**](<#django-the-backend-web-framework>)<br />
&emsp;&emsp;[**Database Setup**](<#Database-Setup>)<br />
&emsp;&emsp;&emsp;&emsp;[SQLite Database Creation](<#SQLite-Database-Creation>)<br />
&emsp;&emsp;&emsp;&emsp;[PostgreSQL Database Creation](<#PostgreSQL-Database-Creation>)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Restoring a Former PostgreSQL Database](<#Restoring-a-Former-PostgreSQL-Database>)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Creating a New PostgreSQL Database](<#Creating-a-New-PostgreSQL-Database>)<br />
&emsp;&emsp;&emsp;&emsp;[Connecting to the Linux VM at Carleton](<#Connecting-to-the-Linux-VM-at-Carleton>)<br />
&emsp;&emsp;&emsp;&emsp;[Django Database Configuration](<#Django-Database-Configuration>)<br />
&emsp;&emsp;[**Environment Setup**](<#environment-setup>)<br />
&emsp;&emsp;&emsp;&emsp;[Core Tool Installation](<#Core-Tool-Installation>)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Installing the Xcode Command Line Tools (macOS only)](<#Installing-the-Xcode-Command-Line-Tools-macOS-only>)<br />
&emsp;&emsp;&emsp;&emsp;[Cloning the repo](<#Cloning-the-repo>)<br />
&emsp;&emsp;&emsp;&emsp;[Homebrew Installation](<#Homebrew-Installation>)<br />
&emsp;&emsp;&emsp;&emsp;[Python3 Installation](<#Python3-Installation>)<br />
&emsp;&emsp;&emsp;&emsp;[SQLite Installation](<#SQLite-Installation>)<br />
&emsp;&emsp;&emsp;&emsp;[PostgreSQL Installation](<#PostgreSQL-Installation>)<br />
&emsp;&emsp;&emsp;&emsp;[Pipenv Installation](<#Pipenv-Installation>)<br />
&emsp;&emsp;&emsp;&emsp;[Dependency Installation from the Pipfile](<#Dependency-Installation-from-the-Pipfile>)<br />
&emsp;&emsp;&emsp;&emsp;[Carleton VPN Installation](<#Carleton-VPN-Installation>)<br />
&emsp;&emsp;&emsp;&emsp;[Environment Setup Troubleshooting](<#Environment-Setup-Troubleshooting>)<br />
&emsp;&emsp;[**Running the Server**](<#running-the-server>)<br />
&emsp;&emsp;&emsp;&emsp;[Server Troubleshooting](<#Server-Troubleshooting>)<br />
&emsp;&emsp;[**Organizational Hierarchy & Nomenclature**](<#organizational-hierarchy--nomenclature>)<br />
&emsp;&emsp;[**The File Hierarchy**](<#the-file-hierarchy>)<br />
&emsp;&emsp;[**Data Flow**](<#data-flow>)<br />
&emsp;&emsp;&emsp;&emsp;[URL mapper](<#url-mapper>)<br />
&emsp;&emsp;&emsp;&emsp;[View](<#view>)<br />
&emsp;&emsp;&emsp;&emsp;[Model](<#model>)<br />
&emsp;&emsp;&emsp;&emsp;[Serializers](<#serializers>)<br />
&emsp;&emsp;&emsp;&emsp;[MVT Architecture](<#mvt-architecture>)<br />
&emsp;&emsp;[**API Endpoints**](<#api-endpoints>)<br />
&emsp;&emsp;&emsp;&emsp;[Testing](<#testing>)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Google id_token Generation](<#google-id_token-generation>)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Sending an HTTP Request](<#sending-an-http-request>)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[Logging in](<#logging-in>)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[GET Requests](<#get-requests>)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[POST Requests](<#post-requests>)<br />
[**References**](<#references>)<br />

# Django: The Backend Web Framework
[Django](<https://www.djangoproject.com>) is a Python [web framework](<https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Web_frameworks>) that is used mainly for backend web development. This document will overview the necessary steps to get Django up and running (setting up the database, setting up the environment on which Django will run, and finally starting the Django server), and will also provide an overview of how Django functions in general and how this project is structured in particular.
## Database Setup
Django requires a connection to a database to be operational. That database can either exist locally on the machine that runs the Django server, or it can exist on another server entirely. By default, Django will create a SQLite database on the machine where the Django server is run. As of version 1.0.0 of this repo, however, a Linux virtual machine (VM) at Carleton is being used to host a PostgreSQL database.
### SQLite Database Creation
If Django is configured to its default settings (shown below), and SQLite is installed (see SQLite Installation in Environment Setup), a new SQLite database will automatically be created on a machine that starts the Django server, unless such a database already exists.

### PostgreSQL Database Creation
If Django is configured to, it can connect to a remote database. Unlike when using SQLite, Django will not create a new database on the remote server running PostgreSQL if the database does not yet exist. As of version 1.0.0 of this repo, a Linux VM (virtual machine) at Carleton is hosting a PostgreSQL database (see next section for how to connect). With the installation of PostgreSQL on a machine, either a previous version of the database used for this project can be restored, or a brand new database can be created. 

#### Restoring a Former PostgreSQL Database
To restore a former PostgreSQL database (i.e., the database used as of version 1.0.0 of this repo), the following steps should be performed:
1. If the Linux VM at Carleton that has been used as of version 1.0.0 of this repo to host the PostgreSQL database is no longer active, a new machine (possible virtual) will need to be setup. It is advised that team members seek the guidance of Mike Tie in performing this step.
2. Install PostgreSQL on the selected (virtual) machine if not already installed
3. Contact Professor Sneha Narayan to obtain access to the file `db_classifieds_v1.out` which contains the data necessary for restoration. Note that this file may contain instructions to restore multiple databases, although only the database "classifieds" is of particular value.
4. [Perform the restoration](https://www.postgresql.org/docs/12/app-pgrestore.html) in accordance with the PostgreSQL documentation

#### Creating a New PostgreSQL Database
If there is no intention to restore a previous version of the database, the following steps should be performed. For further detail, please also refer to this [guide on PostgreSQL use and installation on Ubuntu](<https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04>).
1. `ssh` onto a remote machine as root that will host the database
2. Install PostgreSQL on the remote server
3. Assume the role of the postgres superuser by entering the command `sudo su - postgres`
4. Login to the PostgreSQL database with the command `psql -U postgres`
5. [Create a new user](<https://www.postgresql.org/docs/current/sql-createuser.html>)
6. [Create a new database](<https://www.postgresql.org/docs/current/tutorial-createdb.html>)
7. [Grant privileges](<https://www.postgresql.org/docs/12/ddl-priv.html>) to the new user so they can interact as necessary with the new database (granting access control list values of `CTc` is recommended)
8. Modify Django's database configuration settings as necessary (refer to Database configuration version 2.0 below in the Django Database Configuration section), where in the `DATABASES` constant in `settings.py`, `USER` is set to the name of the user you created, `PASSWORD` is set to the password of the user you created, and `NAME` is set to the name of the database you created.

### Connecting to the Linux VM at Carleton
As of version 1.0.0 of this repo, a Linux VM at Carleton is hosting a PostgreSQL database. This sections provides instructions for connecting to that VM for management and inspection purposes only. These steps are not required for Django to connect to the database (the next section details the necessary configuration instructions).
1. `ssh` onto the remote server at `classifieds.mathcs.carleton.edu` as the user `<classifieds.mathcs.carleton.edu_root_username>` (that is, execute the command `ssh <classifieds.mathcs.carleton.edu_root_username>@classifieds.mathcs.carleton.edu`)--please refer to the note at the top of this file on how to access the username value, among other secure information that is not present explicitly in this repo.
2. Enter the password `<classifieds.mathcs.carleton.edu_root_password>`
3. Assume the role of the postgres superuser by entering the command `sudo su - postgres` (use the same password as above if prompted)
4. Login to the PostgreSQL database with the command `psql -U postgres`
5. List all the databases by entering the command `\l` and notice the database named `classifieds`
6. Connect to the `classifieds` database with the command `\c classifieds`
7. Show all tables in the database by entering the command `\dt`
8. From here, perform instructions using SQL to view or modify contents of this database's relations

### Django Database Configuration
Configuration settings for Django's connection to a database can be found in `classifieds_project/classifieds_project/settings.py`. In particular, is the constant `DATABASES` in `settings.py` that dictates the connection settings. Django's default setting is as follows:
```python
#Database configuration version 1.0
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}
```
As of version 1.0.0 of this repo, the `DATABASES` constant is set as follows to connect to the Linux VM at Carleton:
```python
#Database configuration version 2.0
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'classifieds',
		'USER': '<PostgreSQL_username>',
		'PASSWORD': '<PostgreSQL_user_password>',
		'HOST': 'classifieds.mathcs.carleton.edu',
		'PORT': '',
		'TEST': { #configuration for unit testing
			'NAME': 'classifieds_project_test',

		},
	}
}
```

## Environment Setup
This section provides instructions for how to setup a machine on which the Django server can run. These setup instructions assume that you are working in a linux-based environment (namely, the macOS operating system, Windows Subsystem for Linux in a Windows operating system, or a distro of the Linux operating system itself). Windows users are advised to install [Windows Subsystem for Linux](<https://docs.microsoft.com/en-us/windows/wsl/install-win10>). Readers are advised to sequentially follow the instructions in this "Environment Setup" section, skipping any steps that have already been performed.

If performing these instructions on a Carleton-owned machine, the usage of `brew` (i.e. Homebrew) will not work; such readers are advised to follow the instructions below, but to employ alternate installation methods that do not require `brew`. 

If not performing these instructions on a Carleton-owned machine, the usage of `brew` is critical when following the instructions as written. **Be advised that any deviation from these instructions, including skipping sections for dependencies that may already be installed, may cause unintended consequences.** In particular, any instructions that specify installation of a dependency with `brew` should be followed explicitly; if you installed such a dependency another way, it is advised that you uninstall it and install it again with `brew`. 

### Core Tool Installation
Fundamental tools, especially git, are required for the further setup of the environment. Users of macOS can install the Xcode command line tools which will ensure the installation of all such tools; users of other operating systems are encouraged to install [git](<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>) using a method of their choice, and install any other programs as instructed by the command line interface.

#### Installing the Xcode Command Line Tools (macOS only)
1. Open the application "Terminal"
2. Enter the command `xcode-select --install` (do NOT continue until you have read the next instruction)
3. When prompted, do NOT select "Get Xcode" unless you wish to do so (the file size nears 10 GB and requires considerable time to download and install). Instead, click "Install" which will install only the command line developer tools.

### Cloning the repo
1. In a commmand line interface, navigate to where you wish to clone this repository
2. Clone this repository with the command `git clone <url-of-this-repo>`
3. Note that the default branch is the "master" branch, which your team may designate to hold only tested and stable code. To see the branches available to you, enter the command `git branch`. If you wish to check out a branch other than the master, enter the command `git checkout <branch_name>`. 

### Homebrew Installation
Homebrew is a package manager for Linux-based operating systems (including macOS and those using Windows Subsystem for Linux) which aids in the installation process of various software. It can be installed with the command `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`. Note that the last quote is part of the command itself.

### Python3 Installation
Python 2 is pre-installed on most versions of macOS; Python 3, however, requires installation. Other operating systems will also likely require the installation of Python 3. Python 3 is perhaps most easily installed using the program previous installed, Homebrew. To install Python 3, enter the command `brew install python`.

### SQLite Installation
SQLite can be installed with the command `brew install sqlite3`

### PostgreSQL Installation
PostgreSQL can be installed with the command `brew install postgresql`

### Pipenv Installation
[Pipenv](<https://pypi.org/project/pipenv/>) combines multiple tools together, such as pip and virtualenv. It is particularly helpful when installing dependencies from a list that your team has constructed, all the while using the benefits of a [Python virtual environment](<https://docs.python.org/3/tutorial/venv.html>). Pipenv can be installed by executing `pip3 install pipenv`.

### Dependency Installation from the Pipfile
With pipenv installed, the remaining dependencies can be installed efficiently in a single motion. In a command line interface, begin by navigating to the root directory of the repo, which contains the file "Pipfile" among other contents. Create a Python virtual environment and spawn an associated shell by running the commmand `pipenv shell --three` (note that the argument "three" is specified to make a Python virtual environment for Python3 specifically). To install the dependencies as deliniated in the Pipfile, enter `pipenv install`. Please see troubleshooting note 1 if this fails. Exit the shell (on macOS, use control-D).

### Carleton VPN Installation
As of version 1.0.0 of this repo, connection to the database requires that the machine that runs the Django server has a Carleton ip address. The Django server can not be operationalized without connection to a database. Establishing a Carleton ip address can be achieved by installing and running the VPN that Carleton provides. Please refer to Carleton ITS's [instructions for downloading, installing, and running the VPN](<https://wiki.carleton.edu/display/itskb/GlobalProtect+VPN>). Following installation, please activate the VPN on your machine. This marks the end of the environment setup! Woo hoo! You're well on your way to running the Django server!

### Environment Setup Troubleshooting
Generally, errors during environment setup are due to missing prerequisitive software (including missing the most recent version), or the inability for the machine to find the prerequistive software. The following notes may be helpful generally, and certain parts of the instructions above may refer you to specific notes.
1. The "LIBRARY_PATH" variable may be incorrectly set; if on macOS, run the command `export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/` to allow for the successful installation of psycopg2. Note that closing and reopening a command line session will reset this variable, as will sourcing your .bash_profile or .bash_rc file.
2. "wheel" may be out of date; it can be updated with `pip3 install --upgrade wheel`
3. postgresql may be out of date; it can be updated with `brew upgrade postgresql`

## Running the Server
To run the Django server, perform the following actions:

1. Navigate to `classifieds_project` (the outer project directory; see note 1 in "The File Hierarchy" section below for reference)
2. Start the server with the command `pipenv run python3 manage.py runserver`. Alternatively, you may activate the project's Python virtual enviornment separately with `pipenv shell` and then run `python3 manage.py runserver` inside of the shell. Recall that exiting the shell may require a different key sequence than stopping the server. (On macOS, existing the shell can be accomplished via control-D.)

### Server Troubleshooting
Check for these possible issues when attempting to start and/or access the Django server:
1. If you're connecting to the Linux VM at Carleton to access the PostgreSQL database (which is true as of version 1.0.0 of this repo), you'll need to have the Carleton VPN turned on (or be on campus).
2. By default the Django server is accessed on HTTP port 8000. Verify that when you started the server you did not specify a different port, or if you did, be sure the url you're using to access the Django server reflects that.

## Organizational Hierarchy & Nomenclature
An instance of a collective hierarchy of files whose purpose is to instruct Django for a particular web-app is known as a project (called “classifieds_project” for this project). A project contains at least one app. An app is a collection of files that govern Django’s operation as it relates to a specific domain. The scope of such a domain is variable, and is discretionary. One may elect to consolidate all behavior to a single app, or distribute it across multiple apps. 

This particular project contains an app called “main_app” which houses nearly all of the project’s functionality. This project contains another app called “auth_app” which handles customized user authentication (verifying that a user is who they claim they are) and authorization (determining what a user has permission to do once they have been authenticated). 

Notably the Django nomenclature of an app is distinct from an app in the general term “web app.” A single web app, in which Django can act as the back end, may have many apps (in the Django sense of the word). In addition to one or more apps, a Django project always has a manage.py file, and may optionally have a database contained within the outer project directory.

## The File Hierarchy
\classifieds_project (see note 1)<br />
&emsp;&emsp;manage.py<br />
&emsp;&emsp;\classifieds_project (see note 2)<br />
&emsp;&emsp;&emsp;&emsp;config.py<br />
&emsp;&emsp;&emsp;&emsp;connect.py<br />
&emsp;&emsp;&emsp;&emsp;\resources<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;\google_id_token_gen<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;index.html<br />
&emsp;&emsp;&emsp;&emsp;settings.py<br />
&emsp;&emsp;&emsp;&emsp;urls.py<br />
&emsp;&emsp;&emsp;&emsp;wsgi.py<br />
&emsp;&emsp;\main_app<br />
&emsp;&emsp;&emsp;&emsp;models.py<br />
&emsp;&emsp;&emsp;&emsp;views.py<br />
&emsp;&emsp;&emsp;&emsp;serializers.py<br />
&emsp;&emsp;&emsp;&emsp;admin.py<br />
&emsp;&emsp;&emsp;&emsp;\management<br />
&emsp;&emsp;&emsp;&emsp;\migrations<br />
&emsp;&emsp;&emsp;&emsp;\templates<br />
&emsp;&emsp;&emsp;&emsp;tests.py<br />
&emsp;&emsp;\auth_app<br />
&emsp;&emsp;&emsp;&emsp;models.py<br />
&emsp;&emsp;&emsp;&emsp;views.py<br />
&emsp;&emsp;&emsp;&emsp;custom_auth.py (see note 3)<br />
&emsp;&emsp;&emsp;&emsp;admin.py<br />
&emsp;&emsp;&emsp;&emsp;apps.py<br />
&emsp;&emsp;&emsp;&emsp;\management<br />
&emsp;&emsp;&emsp;&emsp;\migrations<br />
&emsp;&emsp;&emsp;&emsp;\templates<br />
&emsp;&emsp;&emsp;&emsp;tests.py<br />
&emsp;&emsp;db.sqlite3 (see note 4)<br />
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

# References
In the construction of this README.md file and development of this repository, the following sources were consulted:
- [Django documentation: general (Django Software Foundation)](https://docs.djangoproject.com/en/3.0/)
- [Django documentation: customizing authentication (Django Software Foundation)](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/)
- [Django overview (Mozilla Corporation)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
- [Django REST framework: serialization (Encode OSS Ltd.)](<https://www.django-rest-framework.org/api-guide/serializers/>)
- [Googe auth with backend server (Google LLC)](<https://developers.google.com/identity/sign-in/web/backend-auth>)
