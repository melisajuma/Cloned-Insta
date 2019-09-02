# Cloned-Insta
## Author
    Melisa JUma
## Published
* 29/8/2019

## Description
* Cloned-Insta is a premium version of Instagram. In Cloned-Insta, the administrator is not the only one with permisions to post pictures but also the other registered users can do the same as long as they have their accounts.
* It's basically a custom made instagram with fewer features compared to the official instagram application.
* Its simple and easy to use 


## Application Functionality
As a registerd user you can:

1. Make your own profile and edit it the way you want 
2. Post pictures for other registerd users to view, comment or like
3. Search for other registerd users and view their profiles
4. follow other users who can also follow you back



## Installations

1. Clone the repository with:
`git clone https://github.com/Melisajuma/Cloned-Insta
2. You will then have to unzip the zipped format of the repo.

3. You will need to install all dependencies by running this command:
* First make sure your requirements.txt file is like this:

`config==0.3.9`
`dj-database-url==0.5.0`
`Django==1.11`
`django-bootstrap3==10.0.1`
`django-heroku==0.3.1`
`gunicorn==19.9.0`
`Pillow==5.2.0`
`psycopg2==2.7.5`
`python-decouple==3.1`
`pytz==2018.5`
`whitenoise==4.0`
`pip install -r requirements.txt`

* If not use this command:
`pip freeze > requirements.txt`
* i would advice you to use python version 3.6 +
* Do not try to use django version above 1.11, it will result to errors due to compatibility
* For this cause, i recommend python 3.6 but specify `python3.6.8` in your `runtime.txt` file when deploying to heroku

4. To use the application locally you wil have to create a postgress database
follow these steps to get the app up and running:
* in your psql:
`CREATE DATABASE instagram;`
* in your terminal migrate with:
`python3.6 manage.py migrate`
* Make a `.env` file to store your environmental variables

* serve the application with:
`python manage.py runserver`
* open the app on localhost:8000

## Technologies used
1. Django 1.11
2. Python3.6
3. HTML and Css
4. Production deployment to heroku
## License

[This project is licensed under the MIT Open Source license](License).

(c) Melisa JUma
