from django.shortcuts import render , redirect
import openai
from django.contrib.auth.decorators import login_required
openai.api_key = "YOU NEED TO ENTER YOUR OPEN AI KEY"
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer




#function to render home page only if user is logged in
@login_required(login_url='users:login')
def index(request):

    return render(request, 'home/index.html'  )


#function to present all the sorting algoritm
def sorting(request,algorithm):

    #requesting data after submitting the form
    if request.method == "POST":

        #getting user selected programming language
        programingLanguage = request.POST.get("option")

    else:
        programingLanguage = "python"


    #tokens for gpt3 model to generate text
    prompt = f"write simple {algorithm} algorithm in {programingLanguage} programing language with proper indentation"

    #requesting api to generate tokens using text-davinci-001 engine and given prompt message
    response = openai.Completion.create(engine="text-davinci-001" , prompt=prompt , max_tokens=1000 )

    #highlighting programing text data into actual code with proper indentation.
    highlighted_code = highlight(response['choices'][0]['text'], PythonLexer(), HtmlFormatter(style='friendly', linenos=True, noclasses=True))


    #context to pass the algorithm name from user input
    context = {'algorithmname':algorithm , "algorithmcode": highlighted_code , 'programinglanguage' : programingLanguage}
    return render(request, 'home/sorting.html' , context  )