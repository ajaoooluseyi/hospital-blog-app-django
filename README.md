# hospital-blog-app-django

## Description
It is a hospital blog app API built on a SQLite database. It allows Users to register as Doctors or Patients. Doctors are given access to create blog posts and patients can only read. 

### Dependencies

* Django
* Python version 3.10.6 


### Executing program

On the terminal execute the below command to create the projects' working directory and move into that directory.

 
```python
$ mkdir app
cd app
```

In the projects' working directory execute the below command to create a virtual environment for our project. Virtual environments make it easier to manage packages for various projects separately.

 
```python
$ virtualenv venv
```

To activate the virtual environment, execute the below command.

```python
$ source venv/Script/activate
```
Clone this repository in the projects' working directory by executing the command below.

```python
$ git clone https://github.com/ajaoooluseyi/hospital-blog-app-django.git
$ cd hospital-blog-app-django

```

To install all the required dependencies execute the below command.

```python
$ pip install -r requirements.txt
```

To run the app, navigate to the app folder in your virtual environment and execute the command below
```python
$ python manage.py runserver
```

