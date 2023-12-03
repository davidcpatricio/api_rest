# api_rest

* [Django](https://www.djangoproject.com/)
* [DRF](https://www.django-rest-framework.org/)


## Installation
* First make sure you have Python globally installed in your computer. If not, you can get python [here](https://www.python.org).
* After doing this, it is recommended you create a virtual environment for your project.

      $ python -m venv venv

    Note: You can replace the last "venv" with anything else you would like to name your virtual environment
* Then, Git clone this repo to your PC
  
      $ git clone https://github.com/davidcpatricio/api_rest.git

* #### Dependencies
    Cd into your the cloned repo:
  
      $ cd api_rest
  
    Create and fire up your virtual environment:
  
      $ source venv/bin/activate (Mac / Linux)
      $ source venv/Scripts/activate (Windows)
  
    Install the dependencies needed to run the app:
  
      $ pip install -r requirements.txt
  
    Make migrations and migrate
  
       $ python manage.py makemigrations
       $ python manage.py migrate

* #### Run It
    Fire up the server:
  
      $ python manage.py runserver
  
    You can now access the file api service on your browser by using
  
       http://127.0.0.1:8000/
