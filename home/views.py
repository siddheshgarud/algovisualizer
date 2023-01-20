from django.shortcuts import render , redirect

from django.contrib.auth.decorators import login_required


#function to render home page only if user is logged in
@login_required(login_url='users:login')
def index(request):

    return render(request, 'home/index.html'  )


#function to present all the sorting algoritm
def sorting(request,algorithm):

    #context to pass the algorithm name from user input
    context = {'algorithmname':algorithm}
    return render(request, 'home/sorting.html' , context  )