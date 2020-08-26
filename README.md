### Django project create  
`git branch Server`  
`git checkout Server`  
`git rm -fr *`  
`wget https://raw.githubusercontent.com/jpadilla/django-project-template/master/.gitignore`  
  
`python3.8 -m venv env`  
activate environment (Linux: `source env/bin/activate`)  
`pip install django`  
`pip install psycopg2` #posgresql connector  
`pip freeze >requirements.txt`  
  
`django-admin startproject app`  
`cd app`  
change file app/settings.py: 
```  
'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'gd_db',  
        'USER': '',  
        'PASSWORD': '',  
        'HOST': ''  
}  
```  
`python manage.py migrate`  
`python manage.py createsuperuser`  
`python manage.py runserver`  
  
---
### Django project run
`git checkout Server`  
`git pull`  
`python3.8 -m venv env`  
activate environment (Linux: `source env/bin/activate`)  
`pip install -r requirements.txt`  
`cd app`  
`python manage.py runserver`  

http://127.0.0.1:8000/  
  
---
### Інструкція по додаванню сторінки  

#### 1. Файл pages/ulrs.py  
додаємо свій елемент в urlpatterns  


#### 2. Файл pages/views.py  
додаємо фукцію з назвою яку щойно вказали в `pages/ulrs.py`  
не забуваєм додати в data свої дані:  
+ header_h1 - верхній напис в хедері  
+ header_p - нижній  напис в хедері  

#### 3.
вставляємо файл сторінки в templates/pages  
формат:
```
{% extends 'base.html' %}
{% block content %}
верстка
{% endblock %}
```  
#### 3.a 
у верстці міняємо урли  по шаблону:
```html
<img src="{{ STATIC_PREFIX }}img/guarantee/guarantee.jpg" alt="">
```

#### 4
Додаємо урли на свою додану сторінку в файли:  
+ templates/partials/_header.html
+ templates/partials/_header_internal.html
+ templates/partials/_footer.html

#### Робота над помилками
Якщо не грузить якусь картинку, або не та верстка.  
+ Перевірте чи правильний урл до картинки. Чи не забули {{ STATIC_PREFIX }}. Якщо url в css - потрібно пофіксити url в css (додати '/static').  
+ Перевірте чи існує така картинка в app/static/img. Якщо ні - потрібно додати саму картинку.  
+ Якщо не підтягується верстка, нема таких класів як в збірці - потрібно оновити css файл. Взяти зі збірки, з папки dist, main.css і main.css.map, і покласти в static/css  

#### Django compressor
https://django-compressor.readthedocs.io/en/latest/quickstart/  
використовується для зжимання JS, CSS  

#### django-libsass
https://github.com/torchbox/django-libsass  
дає можливість використання scss з Django compressor  
