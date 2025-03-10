

from datetime import datetime
from pyexpat.errors import messages

from django.shortcuts import render, redirect

from .models import Book, Register, Cart, Wishlist, Billing, Payment

def Login(request):
    if request.method == "POST":
            Username = request.POST.get('Username')
            Password = request.POST.get('Password')
            try:
                user = Register.objects.get(Username=Username, Password=Password)
                request.session["User_Id"] = user.User_Id
                if user.Category == 1:
                     return redirect("Home")
                else:
                     return redirect("Merchant")
            except Register.DoesNotExist:
                return render(request, "Login.html", {"Error": "Invalid Username or Password"})

    return render(request, "Login.html")

def Forgot(request):
    if request.method == "POST":
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        ConfirmPassword = request.POST.get('Password1')
        try:
            user = Register.objects.get(Email=Email)
            if Password == ConfirmPassword:
                user.Password = Password
                user.save()
                return redirect("Login")
            else:
                return render(request,"Forgot.html",{"Error":"Password Doesnot Match"})

        except Register.DoesNotExist:
            return render(request,"Forgot.html",{"Error":"Email Doesnot Exist"})
    return render(request,"Forgot.html")

def Add_Book(request):
    if request.method == "POST" and request.FILES['Image'] and "User_Id" in request.session:
        User_Id = request.session["User_Id"]
        User = Register.objects.get(User_Id=User_Id)
        Name = request.POST.get('Name')
        Author = request.POST.get('Author')
        Price = request.POST.get('Price')
        Description = request.POST.get('Description')
        Edition = request.POST.get('Edition')
        Publisher = request.POST.get('Publisher')
        Published = request.POST.get('Published')
        Language = request.POST.get('Language')
        Pages = request.POST.get('Pages')
        Image = request.FILES.getlist('Image')

        Published = datetime.strptime(Published,"%Y-%m-%d").date()
        Book.objects.create(User=User,Name = Name,Author = Author,Price = Price,Description = Description,Edition = Edition,Publisher = Publisher,
                              Published = Published,Language = Language,Pages = Pages,Image=Image)
    return render(request,'AddBook.html')

def Book_Details(request,id):
   t = Book.objects.get(Id=id)
   if request.method == "POST" and request.FILES['Image']:
       t.Name = request.POST.get('Name')
       t.Author = request.POST.get('Author')
       t.Price = request.POST.get('Price')
       t.Description = request.POST.get('Description')
       t.Edition = request.POST.get('Edition')
       t.Publisher = request.POST.get('Publisher')
       t.Published = request.POST.get('Published')
       t.Language = request.POST.get('Language')
       t.Pages = request.POST.get('Pages')
       t.Image = request.FILES.get('Image')
   return render(request,'BookDetails.html',{'t':t})

def Home(request):
   if request.session["User_Id"]:

          User_Id = request.session["User_Id"]
          Sort = request.POST.get('Sort')

          try:
              r = Register.objects.get(User_Id=User_Id)
          except:
              r = None
          wishlist_books = Wishlist.objects.filter(User=User_Id).values_list('Book_id', flat=True)
          r.Heart = bool(wishlist_books)
          if request.method == "POST" and r:
              r.Name = request.POST.get('Name',r.Name)
              r.Email = request.POST.get('Email',r.Email)
              r.Number = request.POST.get('Number',r.Number)
              r.save()

          # Sort elements
          book1 = Book.objects.all()

          if Sort == "name_asc":
               book1 = book1.order_by('Name')
          elif Sort =="name_desc":
              book1 = book1.order_by('-Name')
          elif Sort == "cost_asc":
              book1 = book1.order_by('Price')
          elif Sort == "cost_desc":
              book1 = book1.order_by('-Price')
          else:
              book1 = book1
         # Search
          search = request.POST.get('Search')
          if search:
              book1 = book1.filter(Name__icontains = search)
              if not book1.exists():
                  return render(request, "Home.html", {'Error': 'Item not in list','r': r,
                                                       'search':search})
          else:
              book1 = book1


          return render(request,"Home.html",{'book': book1, 'r': r,'Sort':Sort})

def Update_Book(request,id):
    t = Book.objects.get(Id=id)
    if request.method == "POST" and request.FILES['Image']:
        t.Name = request.POST.get('Name')
        t.Author = request.POST.get('Author')
        t.Price = request.POST.get('Price')
        t.Description = request.POST.get('Description')
        t.Edition = request.POST.get('Edition')
        t.Publisher = request.POST.get('Publisher')
        t.Published = request.POST.get('Published')
        t.Language = request.POST.get('Language')
        t.Pages = request.POST.get('Pages')
        t.Image = request.FILES['Image']
        t.save()
        return redirect('Home')
    return render(request,"UpdateBook.html",{'t':t})

def Delete_Book(request,id):
    y = Book.objects.get(Id=id)
    y.delete()
    return redirect('/')



def Sign_Up(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Number = request.POST.get('Number')
        Category = request.POST.get('Category')
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        ConfirmPassword = request.POST.get('Password1')

        if Password != ConfirmPassword:
            return render(request,'Signup.html',{'error':'Password Doesnot Match'})

        Register.objects.create(Name=Name, Email=Email,Number=Number,Category=Category,Username=Username,Password=Password)
        return render(request,'Login.html')
    return render(request,"SignUp.html")


def Logout(request):
    if "User_Id" in request.session:
      del request.session["User_Id"]
    return render(request,"Login.html")

def Update_User(request,id):
    r = Register.objects.get(User_Id=id)
    if request.method == "POST":
        r.Name = request.POST.get('Name')
        r.Email = request.POST.get('Email')
        r.Number = request.POST.get('Number')
        r.Password = request.POST.get('Password')
        r.save()
    return render(request,"Update.html",{'r':r})

def Add_Cart(request,id):
    if "User_Id" in request.session:
        user = Register.objects.get(User_Id=request.session["User_Id"])
        book = Book.objects.get(Id=id)
        if not Cart.objects.filter(User=user, Book=book).exists():
                Cart.objects.create(User=user,Book=book)
    return redirect("Home")

def View_Cart(request):
    if "User_Id" in request.session:
        user_id = request.session["User_Id"]
        r = Register.objects.get(User_Id=user_id)
        y = Cart.objects.filter(User=user_id)
        total = 0

        if not y:
            print("No cart items found for this user.")
            return render(request, "Cart.html", {'message': 'Your cart is empty.'})
        for i in y:
            total = total + i.Book.Price
        return render(request, "Cart.html", {'book': y,'total':total,'r':r})

def Remove_Cart(request,id):
    if "User_Id" in request.session:
        user_id=request.session["User_Id"]
        cart = Cart.objects.get(User=user_id,Book=id)
        cart.delete()
        return redirect("View_Cart")

def Add_Wishlist(request,id):
    if "User_Id" in request.session:
        user = Register.objects.get(User_Id=request.session["User_Id"])
        book = Book.objects.get(Id=id)
        if not Wishlist.objects.filter(User=user, Book=book).exists():
                   Wishlist.objects.create(User=user,Book=book)

        book.Heart = True
        book.save()
    return redirect("Home")

def View_Wishlist(request):
    if "User_Id" in request.session:
        user_id = request.session["User_Id"]
        r = Register.objects.get(User_Id=user_id)
        y = Wishlist.objects.filter(User=user_id)
        if not y:
            print("No cart items found for this user.")
            return render(request, "Wishlist.html", {'message': 'Your Wishlist is empty.'})
        return render(request, "Wishlist.html", {'book': y,'r':r})

def Remove_Wishlist(request, id):
    if "User_Id" in request.session:
        user_id = request.session["User_Id"]
        book = Book.objects.get(Id=id)
        wishlist = Wishlist.objects.get(User=user_id, Book=book)
        wishlist.delete()
        book.Heart = False
        book.save()
        return redirect("Home")

def Book_Payment(request,id):
    try:
        book = Book.objects.get(Id=id)
    except Book.DoesNotExist:
        return redirect("Home")

    if "User_Id" in request.session and request.method == "POST":
        user_id = request.session["User_Id"]

        try:
            user = Register.objects.get(User_Id=user_id)
        except Register.DoesNotExist:
            return redirect("Login")
        except Book.DoesNotExist:
            return redirect("Home")

        Bill_Name =  request.POST.get('BillName')
        Bill_Email = request.POST.get('Email')
        Bill_Number = request.POST.get('Number')
        Bill_Address = request.POST.get('Address')
        Bill_City = request.POST.get('City')
        Bill_ZipCode = request.POST.get('Zip')
        Bill_Quantity = request.POST.get('Quantity',1)


        Card_Name = request.POST.get('CardName')
        Card_Number = request.POST.get('CardNumber')
        Card_Month = request.POST.get('CardExpiryMonth')
        Card_Year = request.POST.get('CardExpiryYear')
        Card_Cvv = request.POST.get('CardCVV')


        Billing.objects.create(User=user,Book=book,Bill_Name=Bill_Name,Bill_Email=Bill_Email,
                               Bill_Number=Bill_Number,Bill_Address=Bill_Address,Bill_City=Bill_City,
                               Bill_ZipCode=Bill_ZipCode,Bill_Quantity=Bill_Quantity,Bill_Price=book.Price)

        Payment.objects.create(User=user,Book=book,Card_Name=Card_Name,Card_Number=Card_Number,
                               Card_Month=Card_Month,Card_Year=Card_Year,Card_Cvv=Card_Cvv,Price=book.Price)
        return redirect("Home")

    return render(request, 'BookPayment.html',{'book': book })

def View_Order(request):
    if "User_Id" in request.session:
        user_id = request.session["User_Id"]
        r = Register.objects.get(User_Id=user_id)
        y = Billing.objects.filter(User=user_id)
        if not y:
            print("No  items ordered by the user.")
            return render(request, "Ordered.html", {'message': 'Your Order is empty.'})
        return render(request, "Ordered.html", {'book': y,'r':r})

def Merchant(request):
    if "User_Id" in request.session:
        user_id = request.session["User_Id"]
        t = Book.objects.filter(User=user_id)
        try:
            r = Register.objects.get(User_Id=user_id)
        except:
            r = None

        if request.method == "POST" and r:
            r.Name = request.POST.get('Name', r.Name)
            r.Email = request.POST.get('Email', r.Email)
            r.Number = request.POST.get('Number', r.Number)
            r.save()

        return render(request, "Merchant.html", {'book': t, 'r': r})

def Go_Back(request):
    if "User_Id" in request.session:
        user_id = request.session['User_Id']
        user = Register.objects.get(User_Id=user_id)
        if user and Register.Category == '1':
          return redirect("Home")
        else:
            return redirect("Merchant")






    # Create your views here.
