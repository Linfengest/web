from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import reverse,redirect

# Create your views here.
def article_list(request):
    if request.method == 'GET' :
        data = article_model.objects.all()
        return render(request,'article/list.html',{'data':data})

def article(request):
    pass

@login_required()
def write(request):
    if request.method == 'GET':
        form = write_form()
        # print(request.user.username)
        return render(request,'article/write.html',{'form':form})

    if request.method == 'POST':
        form = write_form(request.POST)
        if form.is_valid() :
            article_new = form.save(commit=False)
            article_new.author = request.user
            article_new.save()
            return redirect(reverse("article:list"))

def real_article(request,article_id):
    data = article_model.objects.get(id=article_id)
    return render(request,'article/article.html',{'data':data})
