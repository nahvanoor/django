from django.shortcuts import render
from demoapp. models import *
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Login.objects.get(username=username, password=password)

            request.session['login_id'] = user.id

            if user.usertype == 'admin':
                return HttpResponse('<script>alert("Welcome admin");window.location="/admin_home"</script>')

            elif user.usertype == 'user':
                return HttpResponse('<script>alert("Welcome user");window.location="/user_home"</script>')

            else:
                return HttpResponse('Unknown user type')

        except Login.DoesNotExist:
            return HttpResponse('<script>alert("Invalid username or password");window.location="/login"</script>')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST' and 'submit' in request.POST:
        first = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        state = request.POST['state']
        pincode = request.POST['pincode']

        # ✅ Check if email or phone number already exists
        if Register.objects.filter(email=email).exists():
            return HttpResponse('<script>alert("already existed email");window.location="/register"</script>')

        if Register.objects.filter(phone_number=phone_number).exists():
            # return HttpResponse('phone number already existed')
            return HttpResponse('<script>alert("already existed phonenumber");window.location="/register"</script>')
            

        if Login.objects.filter(username=username).exists():
            # return HttpResponse('username already existed')
            return HttpResponse('<script>alert("already existed username");window.location="/register"</script>')
            

        # ✅ Save login and registration details
        logi = Login(username=username, password=password, usertype='user')
        logi.save()
        reg = Register(
            firstname=first,
            lastname=lastname,
            email=email,
            phone_number=phone_number,
            state=state,
            pincode=pincode,
            LOGIN=logi
        )
        reg.save()

        # messages.success(request, 'You have registered successfully!')
        # return redirect('login')  # Adjust to your URL name
        return HttpResponse('<script>alert("Succesfully Registered");window.location="/login"</script>')
        

    return render(request, 'register.html')

def admin_home(request):
    if 'login_id' not in request.session:
        return redirect('login')
    return render(request, 'admin_home.html')

def user_home(request):
    if 'login_id' not in request.session:
        return redirect('login')
    return render(request, 'user_home.html')
def book(request):
    
    if request.method=="POST" and "submit" in request.POST:
        book_name=request.POST['book_name']
        author_name=request.POST['author_name']
        price=request.POST['price']
        category=request.POST['category']
        image=request.FILES['image']
        
        
        b=Book(book_name=book_name,author_name=author_name,price=price,category=category,image=image)
        b.save()
        
        messages.success(request,'saved successfully!')
    return render(request,'book.html')

def show_book(request):
    m = Book.objects.all()
    return render(request,'show_book.html',{'m':m})


def user_book(request):
    book = Book.objects.all()
    return render(request,'user_book.html',{'book':book})


def updatebook(request,id):
    n = Book.objects.get(id=id)
    if 'update' in request.POST:
        book_name=request.POST['book_name']
        author_name=request.POST['author_name']
        price=request.POST['price']
        category=request.POST['category']
        image=request.FILES['image']
        n.book_name=book_name
        n.author_name=author_name
        n.price=price
        n.category=category
        n.image=image
        n.save()
        messages.success(request,'Updated successfully!')
    return render(request,'updatebook.html',{'n':n})

def delete_book(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    # messages.success(request,'Deleted successfully!') 
    return HttpResponse("Book deleted successfully.")



def menucard(request):
    if request.method=="POST" and "submit" in request.POST:
        image=request.FILES['image']
        name=request.POST['name']
        ingredients=request.POST['ingredients']
        price=request.POST['price']

        
        
        menu=Menucard(image=image,name=name,ingredients=ingredients,price=price)
        menu.save()
        
        return HttpResponse('saved successfully!')
    return render(request,'menucard.html')

def show_menu(request):
    x=Menucard.objects.all()
    return render(request,'show_menu.html',{'x':x})

def user_menu(request):
    menu=Menucard.objects.all()
    return render(request,'user_menu.html',{'menu':menu})


def updatemenu(request,id):
    y = Menucard.objects.get(id=id)
    if 'update' in request.POST:
        image=request.FILES.get('image')
        name=request.POST.get('name')
        ingredients=request.POST.get('ingredients')
        price=request.POST.get('price')
        if image:
            y.image=image
        y.name=name
        y.ingredients=ingredients
        y.price=price
        y.save()
        return HttpResponse('Updated successfully!')
    return render(request,'updatemenu.html',{'y':y})

def deletemenu(request,id):
    menucard= Menucard.objects.get(id=id)
    menucard.delete()
    # messages.success(request,'Deleted successfully!') 
    return HttpResponse("Menu deleted successfully.")


def add_events(request):
    if request.method=="POST" and 'submit' in request.POST:
        event_name=request.POST['event_name']
        event_date=request.POST['event_date']
        start_time=request.POST['start_time']
        end_time=request.POST['end_time']
        total_participants=request.POST['total_participants']
        event_venue=request.POST['event_venue']
        event_location=request.POST['event_location']
        event_ticket_price=request.POST['event_ticket_price']
        event_guest=request.POST['event_guest']
        event_poster=request.FILES['event_poster']
        event=Event(event_name=event_name,event_date=event_date,start_time=start_time,end_time=end_time,total_participants=total_participants,event_venue=event_venue,event_location=event_location,event_ticket_price=event_ticket_price,event_guest=event_guest,event_poster=event_poster)
        event.save()
        messages.success(request,"Submitted Successfully")
    return render(request,'add_events.html')

def show_events(request):
    event=Event.objects.all()
    return render(request,'show_events.html',{'event':event})

def update_events(request,id):
    event=Event.objects.get(id=id)
    if 'update' in request.POST:
        event_name=request.POST.get('event_name')
        event_date=request.POST.get('event_date')
        start_time=request.POST.get('start_time')
        end_time=request.POST.get('end_time')
        total_participants=request.POST.get('total_participants')
        event_venue=request.POST.get('event_venue')
        event_location=request.POST.get('event_location')
        event_ticket_price=request.POST.get('event_ticket_price')
        event_guest=request.POST.get('event_guest')
        event_poster=request.FILES.get('event_poster')
        event.event_name=event_name
        event.event_date=event_date
        event.start_time=start_time
        event.end_time=end_time
        event.total_participants=total_participants
        event.event_venue=event_venue
        event.event_location=event_location
        event.event_ticket_price=event_ticket_price
        event.event_guest=event_guest
        
        if event_poster:
            event.event_poster=event_poster
            
        event.save()
        messages.success(request,"Updated Successfully")
        
    return render(request,'update_event.html',{'event':event})

def user_events(request):
    event=Event.objects.all()
    return render(request,'user_events.html',{'event':event})