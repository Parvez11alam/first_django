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
