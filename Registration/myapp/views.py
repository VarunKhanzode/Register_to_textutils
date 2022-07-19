from django.contrib import messages
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    if (request.method=="POST"):
        loginusername = request.POST["username"]
        loginpassword = request.POST["password"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None :
            login(request,user)
            params = loginusername
            return render(request,'home.html',{'params':params}) 

        else:
            params = "invalid username or password"
            return render(request,'login.html',{'params':params})
    else:
        return render(request,"home.html")

def signup(request):
    return render(request,"signup.html")

def handlesignup(request):
    special_char = ['!','@','#','$','%','^','&','*','(',')','-','=','+','[',']','{','}',';','/','?',',','.',''' " ''',''' ' ''']
    if (request.method=="POST"):
        username = request.POST["username"]
        firstname = str(request.POST.get("fname",False))
        lastname = str(request.POST.get("lname",False))
        email = str(request.POST.get("email",False))
        pass1 = str(request.POST.get("pass1",False))
        pass2 = str(request.POST.get("pass2",False))

        #Username
        if (len(username) > 10):
            params = " Username should be less than 10"
            return render(request,"signup.html",{"params":params})  
        
        check_username_special = check_username_num= 0
        for i in username:
            if i in special_char:
                check_username_special = 1
                break
            if i.isnumeric():
                check_username_num = 1
                break
                
        if (check_username_special!=0):
            params = " Special characters not allowed in username"
            return render(request,"signup.html",{"params":params})
        if (check_username_num!=0):
            params = " Numbers not allowed in username"
            return render(request,"signup.html",{"params":params})

        #First Name
        check_firstname_special = check_firstname_num= 0
        for i in firstname:
            if i in special_char:
                check_flastname_special = 1
                break
            if i.isnumeric():
                check_firstname_num = 1
                break
                
        if (check_firstname_special!=0):
            params = " Special characters not allowed in firstname"
            return render(request,"signup.html",{"params":params})
        if (check_firstname_num!=0):
            params = " Numbers not allowed in ufirstame"
            return render(request,"signup.html",{"params":params})

        #Lastname
        check_lastname_special = check_lastname_num= 0
        for i in lastname:
            if i in special_char:
                check_lastname_special = 1
                break
            if i.isnumeric():
                check_lastname_num = 1
                break
                
        if (check_lastname_special!=0):
            params = " Special characters not allowed in lastname"
            return render(request,"signup.html",{"params":params})
        if (check_lastname_num!=0):
            params = " Numbers not allowed in lastname"
            return render(request,"signup.html",{"params":params})

        #Password
        if ((len(pass1)<6) or len(pass1)>20):
            params = "Password must be 6>password<20 characters"
            return render(request,'signup.html',{'params':params})

        num_check=capital_check=special_check=0
        for i in pass1:
            if (i.isupper()):
                capital_check=1
               
            if (i.isnumeric()):
                num_check=1
            
            if i in special_char:
                special_check=1
               
        if (num_check==0) or (capital_check==0) or (special_check==0):
            params = "Enter atleast one upper letter and one number and  one special character in password"
            return render(request,'signup.html',{'params':params})

        if (pass1!=pass2):
            params = "Passwords doesn't match please re-enter"
            return render(request,'signup.html',{'params':params})




        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request,"SignUp Successfull")
        return render(request,"login.html",{"params":username})
    
    else:
        username = "to LogIn page"
        return render(request,"login.html",{"params":username})



def handlelogin(request):
    if (request.method=="POST"):
        loginusername = request.POST["username"]
        loginpassword = request.POST["password"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None :
            login(request,user)
            return render(request,"utilshome.html") 

        else:
            params = "invalid username or password"
            return render(request,'login.html',{'params':params})
    else:
        return render(request,'login.html')





def handlelogout(request):
    logout(request)
    return render(request,"home.html")


def utilshome(request):
    return render(request,"utilshome.html")

def analyze(request):
    text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    caps = request.POST.get('caps','off')
    nlr = request.POST.get('nlr','off')
    esr = request.POST.get('esr','off')
    temp = text
    if removepunc == "on":
        result = ''
        punctuations = '''!@#$%^&*()_:;,'"./{[]}<>+'''
        for i in text:
            if i not in punctuations:
                result += i
        text = result
        params = {'given':temp,'result':result}
       

    if( caps == "on" ):
        result = ''
        for i in text:
            result += i.upper()
        text = result
        params = {'given':temp,'result':result}
        

    if( nlr == "on"):
        result = ''
        for i in text:
            if (i != "\n" and i != "\r"):
                result += i
        text = result
        params = {'given':temp,'result':result}
        

    if( esr == "on"):
        result = ''
        for i,c in enumerate(text):
            if not(text[i]==" " and text[i+1]==" "):
                result += c 
        text = result
        params = {'given':temp,'result':result}

    if (removepunc=="off" and caps=="off" and nlr=="off" and esr=="off"):
        result = "No Changes"
        params = {'given':temp,'result':result}
        return render(request,'analyze.html',params)
    else:
        return render(request,'analyze.html',params)