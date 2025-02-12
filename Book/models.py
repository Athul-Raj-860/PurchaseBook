from django.db import models



class Register(models.Model):

    User_Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Number = models.CharField(max_length=255)
    Category = models.IntegerField(default=1)
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)

    class Meta:
        db_table="Register"

class Book(models.Model):

    Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    Name = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Price = models.IntegerField()
    Description = models.TextField()
    Edition = models.CharField(max_length=255)
    Publisher = models.CharField(max_length=255)
    Published = models.DateField()
    Language = models.CharField(max_length=255)
    Pages = models.IntegerField()
    Image = models.ImageField(upload_to='upload/')
    Heart = models.BooleanField(default=False)


    class Meta:
        db_table = "Book_Details"

class Cart(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(Register,on_delete=models.CASCADE)
    Book = models.ForeignKey(Book,on_delete=models.CASCADE)

    class Meta:
        db_table="Cart"

class Wishlist(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(Register,on_delete=models.CASCADE)
    Book = models.ForeignKey(Book,on_delete=models.CASCADE)


    class Meta:
        db_table="Wishlist"

class Payment(models.Model):
    Pay_Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE,default=1)
    Card_Name = models.CharField(max_length=255)
    Card_Number = models.CharField(max_length=255)
    Card_Month = models.CharField(max_length=20)
    Card_Year = models.CharField(max_length=10)
    Card_Cvv = models.IntegerField()
    Price = models.IntegerField(default=100)


    class Meta:
        db_table="Payment_Details"

class Billing(models.Model):
    Bill_Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(Register, on_delete=models.CASCADE, default=1)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)
    Bill_Name = models.CharField(max_length=255)
    Bill_Email = models.EmailField(max_length=255)
    Bill_Number = models.CharField(max_length=12)
    Bill_Address = models.TextField()
    Bill_City = models.CharField(max_length=255)
    Bill_ZipCode = models.CharField(max_length=8)
    Bill_Quantity = models.IntegerField()
    Bill_Price = models.IntegerField()

    class Meta:
        db_table="Billing_Details"


# Create your models here.
