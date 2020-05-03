from django.http import HttpResponse
from django.shortcuts import render
import string as st
ab = st.punctuation
print(ab)
def index(request):

   return render(request,'index.html')
    # return HttpResponse('''''')

def analyze(request):
    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc', 'off')

    capital = request.POST.get('capital','off')
    newLine = request.POST.get('newline','off')
    spaceRemover = request.POST.get('spaceRemover','off')
    counter = request.POST.get('characterCount','off')

    if removepunc =="on":
       analyzed = ""
       for char in djtext:
           if char not in ab:
               analyzed = analyzed + char
       params = {"purpose":"remove punctuation","analyzed_text":analyzed}
       djtext = analyzed

       # return render(request,'analyze.html',params)

    if capital == "on":
        analyzed = ""
        for char in djtext:
             analyzed = analyzed + char.upper()
        params = {"purpose": "capitalisation", "analyzed_text": analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if newLine =='on':
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
             analyzed = analyzed +char
        params = {"purpose": "removeNewLine", "analyzed_text": analyzed}
        # return render(request, 'analyze.html', params)
        djtext= analyzed
    if spaceRemover =='on':
        analyzed = ""
        for char in djtext:
            if char !=" ":
             analyzed = analyzed +char
        params = {"purpose": "extraSpacesRemover", "analyzed_text": analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed
    if counter =='on':
        count = 0
        for char in djtext:
            count +=1
        final = f"total no of characters in = {djtext} is {count}"

        params = {"purpose": "characterCounter", "analyzed_text": final}
        # return render(request, 'analyze.html', params)
        djtext=final
    if counter!='on' and spaceRemover !='on' and newLine !='on' and capital != "on" and removepunc !="on" :
        return HttpResponse("Sorry .........please select option")



    return render(request, 'analyze.html', params)


