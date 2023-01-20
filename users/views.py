#All the imports
from django.shortcuts import render , redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from django.contrib import messages



#returns main page of account which isn't developed yet
def index(request):
    return HttpResponse("Hello, world. You're at the pollasss index.")


#fucntion returns sign up page including signing up the new user
def signup_view(request):


    #if user submit the registraion form
    if request.method == "POST":


        #fetching email and password from the registration form
        password= request.POST.get('user-password1')
        email= request.POST.get('user-email')


        #checking if user is already exist or not
        userexist = User.objects.filter( username = email ).exists()

        #if user does not exist then performing registering new user
        if userexist is False:

            #function to create new user with given email and password
            user = User.objects.create_user(email , password = password )
            user.save()
            messages.success(request , message= "Successfully Created New User. Redirected to Login page." , extra_tags="bg-green-100 border border-green-400 text-black-700 px-4 py-3 rounded relative")

            #redirecting user to login page
            return redirect('users:login')
        else:

            #if user is already exist then showing the error
            messages.error(request, {'title':'Email Already Exist','class':"bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" , 'heading':"Error" })





    #rendering the signup html page
    return render(request, 'users/signup.html' )



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
