from django.shortcuts import render,redirect,HttpResponse
from django.core.mail import send_mail
from .forms import *
from .models import *
import random


def index(request):
    return render(request,'index.html')

def home(request):
    if request.method == "POST":
        form = Fo(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.set_pin(form.cleaned_data['pin'])
            account.save()
            return redirect('validate_pin')
    else:
        form = Fo()
    return render(request,'registration.html',{'form':form})

def validate_pin(request):
    balance = None
    id=None
    if request.method == "POST":
        form = PinForms(request.POST)
        if form.is_valid():
            acc_num = form.cleaned_data['acc_num']
            pin = form.cleaned_data['pin']
            try:
                account = Register.objects.get(acc_num=acc_num)
                if account.check_pin(pin):
                    balance = account.balance
                    id=account.id
            except Register.DoesNotExist:
                form.add_error('acc_num','Account not found')
    else:
        form = PinForms()
    return render(request,'login.html',{'form':form,'balance':balance,'total':id})


def withdraw(request,pk):
    data = Register.objects.get(id=pk)
    if request.method == "POST":
        amount = request.POST.get('amount')
        if int(amount) <= data.balance:
            History.objects.create(acc_num = data.acc_num,type = 'withdraw', amt = amount )
            data.balance =data.balance - int(amount)
            data.save()
            return render(request, 'message.html', {'title': 'Successful', 'message': 'Withdraw Successfull'})

        else:
             return render(request, 'message.html', {'title': 'Error', 'message': 'Insufficient balance'})
    return render(request,'options.html')

def deposite(request,pk):
    data = Register.objects.get(id=pk)
    if request.method == "POST":
        amount = request.POST.get('amount')
        History.objects.create(acc_num = data.acc_num,type = 'deposite', amt = amount )
        data.balance =data.balance + int(amount)
        data.save()
        return render(request, 'message.html', {'title': 'Successful', 'message': 'Deposite Successfull'})

    return render(request,'options.html')

def transfer(request,pk):
    data = Register.objects.get(id=pk)
    if request.method == "POST":
        acc = request.POST.get('acc')
        try:
            account = Register.objects.get(acc_num=acc)
            amount = request.POST.get('am')
            History.objects.create(acc_num = data.acc_num,type = 'withdraw', amt = amount )

            if account.acc_num == data.acc_num:
                ...
            else:
                if int(amount) <= data.balance and account.acc_num!=data.acc_num:
                    account.balance+=int(amount)
                    data.balance =data.balance - int(amount)
                    account.save()
                    data.save()
                    return render(request, 'message.html', {'title': 'Successful', 'message': 'Transfer Successfull'})
                else:
                    return render(request, 'message.html', {'title': 'Error', 'message': 'Insufficient balance'})
        except Register.DoesNotExist:
                return render(request, 'message.html', {'title': 'Error', 'message': 'Account number not found'})
    return render(request,'transfer.html')
    
def forgetpin(request):
    account = None
    if request.method == "POST":
        acc = request.POST.get('acc')
        try:
            account = Register.objects.get(acc_num=acc)
            c = s_m(account.mail)
            return redirect('check',c=c,i=account.id)
        except Register.DoesNotExist:
            return render(request, 'message.html', {'title': 'Error', 'message': 'Account number not found'})
    return render(request,'forgetpin.html')

def re_enter(request,pk):
    data = Register.objects.get(id=pk)
    if request.method == "POST":
        np = request.POST.get('new-pin')
        cp = request.POST.get('confirm')
        if np == cp:
            data.set_pin(np)
            data.save()
            return redirect('login')
    return render(request,'re-enterpin.html')


def check(request,c,i):
    account = Register.objects.get(id=i)
    mm = account.mail
    mm = str(mm)
    l = mm.split('@')
    m = l[0][0:2] + '*' * (len(l[0])-2) + l[0][-2::1]+'@'+l[-1]
    d = None
    if request.method == "POST":
        o1 = request.POST.get('o1')
        o2 = request.POST.get('o2')
        o3 = request.POST.get('o3')
        o4 = request.POST.get('o4')
        o5 = request.POST.get('o5')
        o6 = request.POST.get('o6')
        o = o1+o2+o3+o4+o5+o6
        if int(o) == int(c) :
            return redirect('re',pk=i)
        elif account.chances>1:
            account.chances-=1
            account.save()
            d = f'invalid otp chances left {account.chances}'
        else:
            account.chances = 3
            account.save()
            return render(request, 'message.html', {'title': 'Error', 'message': 'Account has be blocked temporarily try after some time'})
    return render(request,'otp.html',{'mail':m,"d":d})


def s_m(m):
    print(m)
    otp = random.randint(100000,999999)
    subject = 'otp to reset your account pin'
    # message = 'We appreciate your submission. Thanks for getting in touch!'
    from_email = 'bobby7793963431@gmail.com'
    recipient_list = [m]
    send_mail(subject,str(otp),from_email,recipient_list)
    return otp


def history(request,pk):
    data = Register.objects.get(id = pk)
    og =  History.objects.filter(acc_num = data.acc_num)
    return render(request,'history.html',{'og':og})

def about(request):
    return render(request,'about_us.html')

def ser(request):
    return render(request,'servies.html')

def con(request):
    return render(request,'contact.html')