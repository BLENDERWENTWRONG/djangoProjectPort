from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import createportfolio
# Create your views here.

def delete(request):
    pass
def view(request):
    return render(request,'portfolio/view.html')
def update(request):
    return render(request, 'portfolio/update.html')

@login_required(login_url="/user/login")
def create(request):
    if request.method=='POST':
        create_from = createportfolio(request.POST,request.FILES)
        if create_from.is_valid():
            instance=create_from.save(commit=False)
            instance.creator=request.User
            instance.save()
    return render(request,'portfolio/create.html')