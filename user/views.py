from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User, UserBio
from .forms import SignupForm, SigninForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.template import context
from django.contrib.auth import logout as django_logout



# Create your views here.

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            signup_form = SignupForm()
            return render(request, 'user/signup.html', {"form": signup_form, 'is_error': False})
        elif request.method == 'POST':
            signup_form = SignupForm(request.POST,request.FILES)
            if signup_form.is_valid():
                # ([signup_form.is_valid(), avatar_form.is_valid()])
                # parent = signup_form.save()
                # parent.save()
                # child = avatar_form.save()
                # child.user = parent
                # child.save()
                # username = signup_form.cleaned_data.get('email')
                # user = User.objects.get(username=username)
                # bio = UserBio(user=user, bio="Click edit to update your profile")
                # bio.save()
                #
                # address = UserAddress(user=user, addres='Tunisia')
                # address.save()
                #
                # avatar = UserAvatar(user=user, avatar="user_images/default.png")
                # avatar.save()

                first_name = signup_form.cleaned_data.get('first_name')
                messages.success(request,
                                 first_name + ', Your account was successfully created! Sign-in to continue.')

                return redirect('signin')

            else:
                return render(request, 'user/signup.html', {"form": signup_form, 'is_error': True})

    else:
        return redirect('create')


def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            signin_form = SigninForm()
            return render(request, 'user/signin.html', {"form": signin_form, 'is_error': False})
        elif request.method == 'POST':
            signin_form = SigninForm(data=request.POST)
            if signin_form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('create')
                else:
                    return render(request, 'user/signin.html', {"form": signin_form, 'is_error': True})
            else:
                return render(request, 'user/signin.html', {"form": signin_form, 'is_error': True})
    else:
        return redirect('create')

@login_required
def logout(request):
    if request.method == 'POST':
            django_logout(request)
            return redirect(sign_in)
