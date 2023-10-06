from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')
    




def rmvPunc(s):
    punct = "!,;.-'\"?"
    res = ""
    for i in s :
      if i in punct :
        continue
      res += i
    return res
def countPunc(s):
    punct = "!,;.-'\"?"
    count=0
    for i in s:
      if i in punct:
         count+=1
    return count

def analyze(request):
    text=request.POST.get('text','Please Enter Some Text !')
    removePunc=request.POST.get('rmvPunc', 'off')
    up=request.POST.get('upper', 'off')
    low=request.POST.get('lower', 'off')
    xtra=request.POST.get('rmvXtraSpc', 'off')
    all=request.POST.get('rmvAllSpc', 'off')
    op=[]
    if(removePunc=="on"):
       text=rmvPunc(text)
       op.append('Removed Punctuations')
    if(up=="on"):
       text=text.upper()
       op.append("Converted to Uppercase")
    if(low=="on"):
       text=text.lower()
       op.append("Converted to Lowercase")
    if(all=="on"):
       text=text.replace(" ", "")
       op.append("Removed All Spaces")
    if(xtra=="on"):
       text=" ".join(text.split())
       op.append("Removed Extra Spaces")
    totalChar=len(text)
    totalWords=len(text.split())
    totalSpace=len(text.split(" "))-1
    totalPunc=countPunc(text)
    return render(request,'analyzed.html',{'text':text,'operations':op,'totalChar':totalChar,'totalWords':totalWords,'totalSpace':totalSpace,'totalPunc':totalPunc})