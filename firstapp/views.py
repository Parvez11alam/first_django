from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h2>Hello world</h2>')
def home(request, id):
    if request.method == 'POST':
        context = {
        'name':request.POST['name']
        }
        return render(request, 'home.html', context)
    '''context = {'value':[44,20,1],
    'id':id}
    if id==3:
        context.update({'name':'parvez'})'''

    return render(request, 'home.html')
def home2(request):
    return render(request, 'home2.html')
def base(request):
    return render(request, 'base.html')
