from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib import messages
from django.template import RequestContext
from formdata.models import student,userdetails
from django.views.decorators.csrf import csrf_exempt
import logging

global_username = "-1"
logging.basicConfig(filename='logsfile.log',format="%(asctime)s %(message)s",level=logging.DEBUG)

def home(request):
    if request.method =='GET':
        return render(request,'home.html')
        logging.debug('Request send to CRUD page')
    elif request.method == 'POST':
        value1 = request.POST['name']
        value2 = request.POST['age']
        value3 = request.POST['branch']
        operation = request.POST['opr']
        
        if operation == "insert":
            stud = student(name=value1,age=value2,branch=value3)
            stud.save()
            logging.info('Data insert to DB')
        elif operation == "update":
            student.objects.filter(name=value1).update(age=value2,branch=value3)
            logging.info('Data updated to DB')
        elif operation == "delete":
            student.objects.filter(name=value1,age=value2,branch=value3).delete()
            logging.info('Data deleted from DB')
        
        output = student.objects.all()
        return render(request,'result.html',{'stud':output})


account_name = ""
@csrf_exempt
def test_view(request):
    global account_name
    if request.method == 'POST':
        purpose = request.POST['purpose']
        # print("--------------------->", purpose)
        # check whether user want login
        if purpose == 'login':
            # print('login')
            email = request.POST['email']
            password = request.POST['password']
            # dbresponse = db_handler(purpose,email,password)
            userdetails_obj = userdetails.objects.filter(email=email,password=password)
            if len(userdetails_obj)==1:
                print('user exits')
                account_name = email
                resp= {'status_code':100,'message':'login successfull','email':account_name}
            else:
                print('new user',email)
                resp = {'status_code':200,'message':'login failed u dont have account'}
        
        # check whether user want enter details
        # elif purpose == 'details':
        #     phone_no = request.GET['phone number']
        #     city = request.GET['city']
        #     obj = userdetails.objects.filter(email=account_name).update(phone_number=phone_no,city=city)
        #     resp = {'status code':100,'message':'details added'}
        # resp = {'status code':200,'message':'for test purpose'}
        print('return',account_name)
        return JsonResponse(resp,safe=False)
    else:
        print('_______________________>request got')
        purpose = request.POST['purpose']
        print("----------------->",purpose)
        resp = {'status_code':200,'message':'reached to first project'}
        return JsonResponse(resp)
        

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        obj = userdetails.objects.filter(email=email)
        if len(obj)==0:
            if password == repassword:
                global global_username
                global_username = username
                newobj = userdetails(username=username,email=email,password=password)
                newobj.save()
                logging.info('New user Registerd '+username)
                return render(request,'basedetails.html',{'uname':username})
            else:
                messages.info(request,'both passwords should be same!')
                logging.error('user entered both passwords different')
                return redirect('signup')
        else:
            messages.info(request,'account already exits')
            logging.error('Account already Exits')
            return redirect('login')
    
def basedetails(request):
    if request.method == 'GET':
        logging.debug('base details page called')
        return render(request,'basedetails.html')
    elif request.method == 'POST':
        ph_number = request.POST['phno']
        city_name = request.POST['city']
        state_name = request.POST['state']
        obj = userdetails.objects.filter(username=global_username).update(phone_number=ph_number,city=city_name,state=state_name)
        logging.info('basic details entered by user:'+global_username)
        return render(request,'login.html')    

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
        logging.debug('Login page called')
    elif request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        obj = userdetails.objects.filter(username=uname,password=password)
        if len(obj):
            messages.info(request,'welcome '+uname)
            logging.info('User logged in= '+uname)
            return redirect('home')
        else:
            messages.info(request,'please Sign in')
            logging.error('User Account not Exits')
            return redirect('login')
