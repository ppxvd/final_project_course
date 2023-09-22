from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from django.shortcuts import render
from .forms import CommentForm

def blog(request):
    return render(request, 'main_app/blog.html')

def category(request):
    return render(request, 'main_app/category.html')

def category2(request):
    return render(request, 'main_app/category2.html')

def contact(request):
    return render(request, 'main_app/contact.html')

def create_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main_app/create_an_account.html', {'form': form})

def redirect_to_registration(request):
    return redirect('auth_comments_app:create_an_account.html')

def redirect_to_login(request):
    return redirect('auth_comments_app:login.html')

def home(request):
    return render(request, 'main_app/home.html')

def order_info(request):
    return render(request, 'main_app/order_info.html')

def shopping_cart(request):
    return render(request, 'main_app/shopping_cart.html')

def text_page(request):
    return render(request, 'main_app/text_page.html')

def products_page(request):
    comments = Comment.objects.all()
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.save()
            return redirect('products_page')
    else:
        comment_form = CommentForm()

    return render(request, 'main_app/products_page.html', {'comments': comments, 'comment_form': comment_form})

def products_page_notepade(request):
    comments = Comment.objects.all()
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.save()
            return redirect('products_page_notepade')
    else:
        comment_form = CommentForm()

    return render(request, 'main_app/products_page_notepade.html', {'comments': comments, 'comment_form': comment_form})

def products_page_pc(request):
    comments = Comment.objects.all()
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.save()
            return redirect('products_page_pc')
    else:
        comment_form = CommentForm()

    return render(request, 'main_app/products_page_pc.html', {'comments': comments, 'comment_form': comment_form})

def products_page_redmi(request):
    comments = Comment.objects.all()
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.save()
            return redirect('products_page_redmi')
    else:
        comment_form = CommentForm()

    return render(request, 'main_app/products_page_redmi.html', {'comments': comments, 'comment_form': comment_form})

def products_page_monitor(request):
    comments = Comment.objects.all()
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.save()
            return redirect('products_page_monitor')
    else:
        comment_form = CommentForm()

    return render(request, 'main_app/products_page_monitor.html', {'comments': comments, 'comment_form': comment_form})















