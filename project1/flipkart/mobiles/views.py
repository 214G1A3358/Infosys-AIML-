#views.py
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from mobiles.service import client

# Create your views here.
def func1(request):
   sentences=[
       {"name":"peanuts","price":300},
       {"name":"jaggery","price":200},
       {"name":"cashew","price":400}
   ]
   
   return render(request,"index.html", {'Food':sentences})


#return render(request,"index.html", {'sentences':sentence})

   
   # student="hi hello"
   # context={"message":"student"}
   #good_students=[
    #  {'name':"Nandu","mobile":"8142270194","rollno":"3366"},
    #  {'name':"Mouni","mobile":"6302489632","rollno":"3358"},
    #  {'name':"Chandrika","mobile":"7860128774","rollno":"3314"},
    #  {'name':"Kavya","mobile":"87268295554","rollno":"3342"}
   #]


   
def func2(request):
    documents = [
        "Eating chicken is not good for health ",
        "mutton and fish are quite good to eat",
        "eggs are very good"
    ]
    result=client.analyze_sentiment(documents=documents)
    li=[]
    for c,r in zip(documents,result):
        d={'comment':c,"review":r.sentiment}
        li.append(d)
    return render(request,"about.html",{"res":li})
def func3(request):
    return render(request,"subapp.html") #contach.html