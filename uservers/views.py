from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, PostForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from uservers.models import Post,User
from django.contrib.auth.mixins import LoginRequiredMixin

# from productvers.models import Product
# Create your views here.


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f" {user.email} Already authenticated")
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email')
            # raw_passw =  form.cleaned_data.get('password1')
            # user = authenticate(email=email, password=raw_pass)
            # login(request, user)
            # destination = kwargs.get("next")
            # if destination:
            #     return redirect(destination)
            return redirect("home")
        else:
            context['registration_form'] = form
    return render(request, 'uservers/register.html', context)


def logout_view(request):
    logout(request)
    return redirect("home")


def login_view(request, *args, **kwargs):

    user = request.user
    if user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    return redirect('register')

    return render(request, 'uservers/login.html')

@login_required(login_url='login')
def PostCreateView(request):
    form = PostForm()
    if request.method == "POST":
        if request.user.is_authenticated:
            form = PostForm(request.POST)
            
            for field in form:
                print(field.value())
            if form.is_valid():
                new_post=Post.objects.create(
                    user=User.objects.get(pk=request.user.id),
                    text=form.cleaned_data["text"]


                    )
                new_post.save()
                return redirect('success')

            else:
                print("ERROR")
                print(form.errors)

    context = {'form':form}
    return render(request, 'uservers/createpost.html',context)



def home(request):
    posts = Post.objects.all()
    users = User.objects.all()
    context = {'posts':posts,'users':users}
    return render(request, 'uservers/home.html', context)

def success_msg(request):
    return render(request,'uservers/success.html')

@login_required(login_url='login')
def myPosts(request,pk):
    userall = User.objects.get(id=pk)
    posts = userall.post_set.all()
    context = {'posts': posts}
    return render(request, 'uservers/mypost.html', context)
