from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Report_issue,Safty_instruction
def home(request):
    return render(request,'home.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('home')
        else:
           messages.error(request,'please check the details properly')
           return redirect('login')
    return render(request,'user.html')
def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"sorry you'r not admin/staff")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'admin.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def Register_view(request):
    if request.method =='POST':
        First_Name = request.POST['Name']
        Email=request.POST['email']
        username =request.POST['username']
        password =request.POST['password']
        confirmation_password =request.POST['cnfm_password']
        select_user=request.POST['select_user']
        if select_user == 'admin':
            select_user=True
        else :
            select_user=False
        if password == confirmation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'register.html')
def dashboard_view(request):
    alerts=Safty_instruction.objects.all()
    reports=Report_issue.objects.all()
    return render(request,'residence.html',{'alerts':alerts,'Reports':reports})
def report(request):
    if request.method=="POST":
        Incident=request.POST['incident_type']
        Location=request.POST['location']
        Description=request.POST['description']
        data = Report_issue.objects.create(Report_by=request.user,Incident=Incident,Location=Location,Description=Description)
        data.save()
    return redirect('dashboard')
def instruction(request):
    if request.method=="POST":
        Title=request.POST['title']
        Details=request.POST['detail']
        data=Safty_instruction.objects.create(Title=Title,Details=Details)
        data.save()
    return redirect('dashboard')
def New_instruction(request):
    return render(request,'addinstruction.html')
def delete_report(request,pk):
    data=Report_issue.objects.get(id=pk)
    data.delete()
    return redirect('dashboard')
        