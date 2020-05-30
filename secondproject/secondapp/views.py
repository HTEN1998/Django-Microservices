from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.

# takes data from request and send to microservices1
@csrf_exempt
def getuserdetails(request):
    if request.method == 'GET':
    
        purpose = request.GET['purpose']
        if purpose == 'login':
            email = request.GET['email']
            password = request.GET['password']
            return HttpResponseRedirect('http://localhost:8000/test_view?email='+email+'&password='+password+'&purpose='+purpose)
        else:
            phno = request.GET['phone number']
            city = request.GET['city']
            return HttpResponseRedirect('http://localhost:8000/test_view?phone number='+phno+'&city='+city+'&purpose='+purpose)

    else:
        # print("--------------------------->")
        purpose =request.POST['purpose']
        email = request.POST['email']
        password = request.POST['password']
        

        post_data = {'purpose':purpose,'email':email,'password':password}
        response = requests.post('http://localhost:8000/test_view',data = post_data)

        print("purpose---------->",purpose)
        print("email---------->",email)
        print("password---------->",password)

        print("---------->response= ",response.json())
        # resp = {'status code':200, 'message':'welcome back to second app'} 
        
        return JsonResponse(response.json())