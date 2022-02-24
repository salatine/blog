# blog

![image](https://user-images.githubusercontent.com/95940523/155431283-b3341cf1-825b-4519-92dc-f45a793bc870.png)
![image](https://user-images.githubusercontent.com/95940523/155431716-8749b5b8-c80f-403e-a8fe-b78508e4b447.png)

A simple news' blog website written in Portuguese, where you can make new posts (and comment on them) from Django Admin section.
This website uses:
- Django
- Django Summernote
- Pillow
- MySQL (both python module and database)
- HTML and CSS
- Bootstrap

## Setup

First, clone this project onto a new folder (make sure you have Git installed) and move to it. Once in the project's folder, create a virtual environment, called "venv".
```
$ git clone https://github.com/salatinee/blog.git
$ cd blog
$ python -m venv venv
```

And activate it, for Linux or Windows, respectively:
```
$ python venv/bin/activate # if you have Linux do this
$ python venv/Scripts/activate.ps1 # if you have Windows do this
```

After that, we can install the requirements to run the application.
```
$ pip install -r requirements.txt
```

Also, we are going to need to migrate data to the project's database, and create a 'superuser', to have access to Django's Admin page and create posts:
```
$ python manage.py migrate
$ python manage.py createsuperuser
```

Everything is ready! Now you can access it by the following command:
```
$ python manage.py runserver
```
It should output something like: <br>
`Django version 4.0, using settings 'blog.settings'`<br>
`Starting development at localhost:8080`<br>
`Quit the server with CTRL-BREAK.`

Now, to create posts, we need to access Django's Admin page. To do that, just access the link provided and add '/admin' after it. And fill in the superuser values you previously entered. Afterwards, you can click on Posts and start making posts for the news' blog:

![image](https://user-images.githubusercontent.com/95940523/155452480-69330273-f5ee-46d1-8c9e-759e70336b7b.png)
