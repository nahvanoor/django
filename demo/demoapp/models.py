from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    
    
class Register(models.Model):
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    address=models.CharField(max_length=500)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=50)

class Book(models.Model):
    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    
    
class Menucard(models.Model):
    image=models.ImageField(upload_to='menu_images/',null=True, blank=True)
    name=models.CharField(max_length=100)
    ingredients=models.CharField(max_length=500)
    price=models.CharField(max_length=100)

class Event(models.Model):
    event_name=models.CharField(max_length=50)
    event_date=models.CharField(max_length=50)
    start_time=models.CharField(max_length=50)
    end_time=models.CharField(max_length=50)
    total_participants=models.CharField(max_length=50)
    event_venue=models.CharField(max_length=50)
    event_location=models.CharField(max_length=100)
    event_ticket_price=models.CharField(max_length=50)
    event_guest=models.CharField(max_length=50)
    event_poster=models.ImageField(upload_to="event_posters/",null=True,blank=True)
    
    