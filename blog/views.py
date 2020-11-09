from django.shortcuts import redirect, render
from .models import Article
from .forms import TextEditForm

def home(request):
    texts = Article.objects.all()
    return render(request, 'home.html', {'texts': texts})


def add(request):
    if request.method == 'POST':
        form = TextEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TextEditForm()
    return render(request, 'add.html', {"form": form})