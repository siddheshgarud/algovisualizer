
from django.shortcuts import render , redirect
from django.http import HttpResponse
import math , random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib import messages



#returns main page of account which isn't developed yet
def index(request):
    return HttpResponse("Hello, world. You're at the pollasss index.")



#function to generate random otp
def generateOTP():
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP


#function to send email to user entered email with generated otp
def sent_mail(request , email , genertated_otp):

    #html format
    htmlgen = f'<p>Your OTP is <strong>{genertated_otp}</strong></p>'

    #send email
    send_mail('Your requested OTP',genertated_otp,'AlgorithmVisualizer',[email], fail_silently=False, html_message=htmlgen)



#fucntion returns sign up page including signing up the new user
def signup_view(request):

    #if user submit the registraion form
    if request.method == "POST":

        #fetching user otp if otp form is submitted
        user_otp = request.POST.get("user-otp")
        if user_otp:

            #if otp for,is submitted then fetching genereted data from session
            generated_otp = request.session.get("generated_otp")

            #if user entered otp and generated otp is same then fetching email an password from session and saving the new user
            if(user_otp == generated_otp):
                email = request.session.get("email")
                password = request.session.get("password")


                user = User.objects.create_user(email , password = password )
                user.save()
                messages.success(request , message= "Successfully Created New User. Redirected to Login page." , extra_tags="bg-green-100 border border-green-400 text-black-700 px-4 py-3 rounded relative")

                return redirect('users:login')
            else:
                messages.error(request , message= "Wrong OTP" , extra_tags="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative")





        #fetching email and password from the registration form
        password= request.POST.get('user-password1')
        email= request.POST.get('user-email')

        request.session["email"] = email
        request.session["password"] = password

        #checking if user is already exist or not
        userexist = User.objects.filter( username = email ).exists()

        #if user does not exist then performing registering new user
        if userexist is False:

            #genereated otp
            generated_otp=generateOTP()

            #sending email with otp
            sent_mail(request , email , generated_otp)

            #storing generated otp in session
            request.session["generated_otp"] = generated_otp

            return render(request, 'users/verification.html'  )

        else:

            #if user is already exist then showing the error
            messages.error(request, {'title':'Email Already Exist','class':"bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" , 'heading':"Error" })


    context = {'otpverificationwindow' : "none" }
    return render(request, 'users/signup.html' , context )




#function to return login view page with login the given user
def login_view(request):


    #if user submit the login form
    if request.method == "POST":

        #fetchinng password and email from given user input
        password= request.POST.get('user-password1')
        email= request.POST.get('user-email')


        #checking if user is arleady exist or not
        userexist = User.objects.filter( username = email ).exists()

        #if user does not exist then showing error
        if userexist is False:

            messages.error(request , message= "Email is not Registered" , extra_tags="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative")

        else:

            #if user is exist and authentiation complete successfully then login the user and redireting user to home page
            user =  authenticate(request,username=email , password=password)

            if user is None:
                messages.error(request , message= "Password Does not match" , extra_tags="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative")
            else:
                login( request , user)
                messages.success(request , message= "Successfully Login with given credentials" , extra_tags="bg-green-100 border border-green-400 text-black-700 px-4 py-3 rounded relative")
                return redirect('home:index')


    #rendering login html page
    return render(request, 'users/login.html' )




#function to logout the user and redirectinng to login page
def logout_view(request):
    logout(request)
    return redirect('users:login')
