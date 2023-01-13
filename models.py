from django.db import models

class Sign_In(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self) :
        return self.first_name

    
    
class expense_management(models.Model):
    expense=models.CharField(max_length=100)
    date=models.DateTimeField()
    amount=models.IntegerField()
    description=models.TextField(max_length=1300)
    Sign_In=models.ForeignKey(Sign_In, blank=True,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.expense


class expense_management(models.Model):
    expense=models.CharField(max_length=100)
    date=models.DateTimeField()
    amount=models.IntegerField()
    description=models.TextField(max_length=1300)
    Sign_In=models.ForeignKey(Sign_In, blank=True,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.expense

class expense_management(models.Model):
    expense=models.CharField(max_length=100)
    date=models.DateTimeField()
    amount=models.IntegerField()
    description=models.TextField(max_length=1300)
    Sign_In=models.ForeignKey(Sign_In, blank=True,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.expense
