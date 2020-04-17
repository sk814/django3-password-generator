from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')
def FeedbackForm1(request1):
    character= list('abcdefghijklmnopqrstuvwxyz')

    if request1.GET.get('Uc'):
        character.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request1.GET.get('numbers'):
        character.extend('123456789')
    if request1.GET.get('Letters'):
        character.extend('RajRaj')
    if request1.GET.get('Specialchar'):
        character.extend('!@#$%^&*()_+')


    length=int(request1.GET.get('length',12))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(character)

    return render(request1, 'generator/InsideForm.html',{'password':thepassword})

def review(request):
    return render(request,'generator/Review.html')
