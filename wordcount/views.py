from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(Request):
    return render(Request, 'home.html')

def count(Request):
    COUNT1 = Request.GET['USERTEXT']
    WORDCOUNT = COUNT1.split()
#PARAMETER FOR DICTIONARY
    worddictionary = {}
#FOR LOOP
    for word in WORDCOUNT:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(Request, 'count.html',{'COUNT1':COUNT1,'COUNT2':len(WORDCOUNT),'worddictionary':sortedwords})

def about(Request):
    return render(Request, 'about.html')
