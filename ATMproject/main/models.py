from django.db import models
from django.contrib.auth.hashers import make_password, check_password



class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender
    
class Acc_type(models.Model):
    acc_type = models.CharField(max_length=20)

    def __str__(self):
        return self.acc_type

class Register(models.Model):
    acc_num = models.BigIntegerField(unique=True,editable=False)
    eny_pin = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    acc_type = models.ForeignKey(Acc_type,on_delete=models.CASCADE)
    mail = models.EmailField(unique=True)
    chances = models.IntegerField(default=3)

    def save(self,*args,**kwargs):
        if not self.pk:
            last_account = Register.objects.order_by('-acc_num').first()
            if last_account:
                self.acc_num = last_account.acc_num + 1
            else:
                self.acc_num = 1234567891
        super().save(*args,**kwargs)


    def set_pin(self,pin):
        self.eny_pin = make_password(pin)
        self.save()
    
    def check_pin(self,pin):
        return check_password(pin,self.eny_pin)
    

    def __str__(self):
        return f"account balance {self.acc_num}"
class History(models.Model):
    acc_num = models.BigIntegerField()
    type = models.CharField(max_length=50)
    amt = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        yield self.acc_num,self.type,self.amt 