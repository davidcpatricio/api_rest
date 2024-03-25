# api_rest

This project was made using the following tools:
* [Django] 4.2.7 (https://www.djangoproject.com/)
* [DRF] 3.14.0 (https://www.django-rest-framework.org/)


## Installation
* First make sure you have Python globally installed in your computer. If not, you can get python [here](https://www.python.org).
* After doing this, it is recommended you create a virtual environment for your project.

      $ python -m venv venv

    Note: You can replace the last "venv" with anything else you would like to name your virtual environment
* Then, Git clone this repo to your PC
  
      $ git clone https://github.com/davidcpatricio/api_rest_django.git

* #### Dependencies
    Activate your virtual environment:
  
      $ source venv/bin/activate (Mac / Linux)
      $ source venv\Scripts\activate (Windows)

   Cd into your the cloned repo:
  
      $ cd api_rest
  
    Install the dependencies needed to run the app:
  
      $ pip install -r requirements.txt
  
    Create a superuser in Django Admin using the following command:
  
       $ python manage.py createsuperuser

* #### Run It
    Fire up the server:
  
      $ python manage.py runserver
  
    You can now access the file api service on your browser by using
  
       http://127.0.0.1:8000/

  In order to visualize the data, just log in with your username and password created before.
