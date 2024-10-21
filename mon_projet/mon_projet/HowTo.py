# installing the Django Framework with pip install
pip install django

# creating a Django project
django-admin startproject mon_projet

# Django project program is made up of multiple apps :
# We've created a sample app (which deals with users)
python manage.py startapp users_app  

# add your app to the app list of the Django project
# in the file settings that is under mon_projet add the following to the INSTALLED_APPS vector
INSTALLED_APPS = [
    'users_app',
]
# Creating a user model (we extended the default model of django for instance add email)
--> editing the users_app/models.py file (adding the class CustomUser(AbstractUser):)
# once the model is created, it has to be registered on the admin.py file
--> editing the users_app/admin.py file (admin.site.register(CustomUser, UserAdmin))

# to create a view (endpoint presenting some data) 
# you have to create it in Views file under the app (as class based CBV)
--> editing the users_app/views.py example with the function ²²user_list²²
--> see also the index view (def index ) and its corresponding path in urls file

## Setting the URL to expose a created view, add the path to the users_app/urls.py
urlpatterns = [
    path('users/', views.user_data, name='user_data'),
]

## when performing changes to your app, run the migrations Commands from powershell :
#Run migrations to set up the database: 
python manage.py makemigrations
python manage.py migrate

## two separate concepts are used in Django to separate between schema data and actual instance data
# Those are 
Migrations --> all the operations that alter Add, remove existing or new models (classes that represent tables)
Fixtures --> Data loaded as serialized data like json file, XML or Yaml