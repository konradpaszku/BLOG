from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogForm

# Create your views here.
def index(request):
    """Strona główna"""
    posts = BlogPost.objects.all().order_by('-date_added')
    context = {'posts': posts} 
    return render(request, 'blogs/index.html', context)
@login_required
def new_post(request):
    """Dodanie nowego postu"""
    if request.method != 'POST':
        #Nie przekazano żadnej treści nalezy utworzyc pusty formularz
        form = BlogForm()
    else:
        #Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    #Wyswietlenie pustego formularza
    context = {'form': form, }
    return render(request, 'blogs/new_post.html', context)
@login_required
def edit_post(request, pk):
    """Edycja postu"""
    post = get_object_or_404(BlogPost, pk=pk)
    title = post.title
    if request.method != 'POST':
        #żądanie początkowe, wypełnianie formularza aktualną treścią wpisu.
        form = BlogForm(instance=post)
    else:
        form = BlogForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'title': title, 'post': post, 'form':form}
    return render(request, 'blogs/edit_post.html', context)
@login_required
def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blogs/post_detail.html', {'post': post})
