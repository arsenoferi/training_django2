from django.http import HttpResponse
from django.shortcuts import render
import operator
#test
def Home(request):
    return render(request,'home.html',{'seno' : 'My Name Is Seno'})

def About(request):
    variabel={
        'Nama':'Arseno Feri Alzahabi',
        'Jobs': 'Compliance Auditor'
    }
    return render(request,'about.html', variabel)

def Count(request):
    allinput = request.GET['allinput']
    
    wordlist = allinput.split()
    
    worddict = {}
    
    for word in wordlist:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word] = 1
            
    count_worddict = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    
    nilai = {
       'fulltext':allinput,
       'count' : len(wordlist),
       'worddict' : count_worddict
    }
    
    return render(request,'count.html', nilai)
