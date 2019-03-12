# RSSFeed-DjangoVueJS

Tutorial from:
https://utan.io/lessons/lets-make-an-rss-reader.html

Youtube Video from:
https://www.youtube.com/watch?v=0FTaWat_VsM

# Installation
mkdir venv && virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

# Folder Structure
```
RSSFeed-DjangoVueJS
  ├── venv
  ├── requirements.txt
  └── rssreader
    ├── manage.py
    ├── rssreader
    └── rss
      ├── urls.py
      ├── templates
      │  └── rss
      │      ├── base.html
      │      ├── control.html
      │      ├── feeds.html
      │      └── reader.html
      └── static
         └── rss
            └── app.js 
```

## Test Apps
python manage.py test rss

## Run Server
python manage.py runserver

## Open on Browser
http://127.0.0.1:8000/rss/

# Useful Documentation:

virtualenv
https://sourabhbajaj.com/mac-setup/Python/virtualenv.html

Django REST Framework
https://www.django-rest-framework.org/

Vue JS
https://vuejs.org/

Bootstrap
https://getbootstrap.com/
