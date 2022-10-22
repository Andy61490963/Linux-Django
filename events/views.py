from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import homepost
from .models import Interest
from .models import information
from .models import paper
from .models import all_aboutus
from .models import Portfolio
from .forms import InformationForm
from .paperforms import paperForm
from django.shortcuts import redirect

def My_Portfolio(request):
    Portfolios = Portfolio.objects.all()
    return render(request,'Portfolio.html',
        {"Portfolios":Portfolios},)

def aboutus(request):
    aboutus1 = all_aboutus.objects.all()
    return render(request,'aboutus.html',
        {"aboutus1": aboutus1},)

def add_paper(request):
    submitted = False
    if request.method == "POST":
        form = paperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_paper?submitted=True')
    else:
        form = paperForm
        if 'submitted' in request.GET:
            submitted =  True
        
    return render(request,'add_paper.html',
        {'form': form, 'submitted': submitted})

def all_paper(request):
    papers = paper.objects.all()
    return render(request,'paper.html',
        {"papers": papers},)
    
def delete_information(request, information_id):
    update_information = information.objects.get(pk=information_id)
    update_information.delete()
    return redirect('infoname-list')

def update_information(request, information_id):
    update_information = information.objects.get(pk=information_id) #在model中找id
    form = InformationForm(request.POST or None, request.FILES or None, instance=update_information)
    if form.is_valid():
        form.save()
        return redirect('infoname-list')
        
    return render(request,'update_information.html',
        {"update_information": update_information,
        'form':form})

def search_information(request):
    if request.method == "POST":
        searched = request.POST['searched'] #受到來自使用者的請求
        informations = information.objects.filter(name__contains=searched)
        
        return render(request,
        'search_information.html',
        {'searched':searched,
        'informations':informations})
    else:
        return render(request,
        'search_information.html',
        {})
    
def show_information(request, information_id):
    infodetail = information.objects.get(pk=information_id)
    return render(request,'show_information.html',
        {"infodetail": infodetail})

def infoname_list(request):
    infoname_list = information.objects.all()
    return render(request,'information.html',
        {"infoname_list": infoname_list})

#Django form function
def add_information(request):
    submitted = False
    if request.method == "POST":
        form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_information?submitted=True')
        
    else:
        form = InformationForm
        if 'submitted' in request.GET:
            submitted = True
          
    return render(request,'add_information.html',
        {'form': form, 'submitted': submitted}) #add_information.html與views.add_information對應

#info function
def all_info(request):
    info = information.objects.all()#.order_by('-name')
    return render(request,'info.html',
        {"info": info},)

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    post = homepost.objects.all()#.order_by('-name')
    name = "Sentimental1"
    #time
    now = datetime.now()
    time = now.strftime("%Y-%m-%d, %H:%M")
    return render(request,
        'home.html', {
        "post": post,
        "name": name,
        "year": year,
        "month": month,
        "time": time,
        })