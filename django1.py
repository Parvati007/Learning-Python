#DJANGO
#django is free and open source web application framewoork written in python
#django offers a big collection of modules which you can use in your own projects
#save a lot time for developers

#INSTALLING DJNAGO
#pip install django

#CREATE PROJECT
#djnago-admin startproject projectName

#CREATE APP
#python manage.py startapp appname

#STARTING SERVER
#python manage.py runserver

#---------------------------------------------------------------------------------------------------------
#MVT Architecture of django...........software design pattern
#Model:- DATABASE
#View:-  LOGIC
#Template:- PRESENTATION

#user----------django-----url----view------(1)model---(2)template
#View is used to execute the business logic and interact with a model to carry data and render templates
#there is no separate controllers

#---------------------------------------------------------------------------------------------------------
#URL Dispatching
#hello/urls.py----------->home/urls.py-------------->home/views.py---------->run the functions/render

#---------------------------------------------------------------------------------------------------------
#STATIC FILES
#static files in djnago are css, js and image files stored in static/ directories
#they are configured with STATIC_URL served in development automatically
#NOTE:- public ya sensitive info nhi dalna in files me

#---------------------------------------------------------------------------------------------------------
#TEMPLATES IN DJANGO
#templates are HTML files that define the structure and layout of the web pages in django application
#DTL = DJANGO TEMPLATE LANGUAGE
#DRP = DON'T REPEAT YOURSELF
#{{variable}}.....you access like this in html file.
