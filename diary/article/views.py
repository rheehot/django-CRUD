from django.shortcuts import render
from article.models import Article

# Create your views here.
def index(request):
    queryset = Article.objects.all()
    context = {
        'articles': queryset,
    }
    return render(request, 'article/index.html', context=context)

def create(request):
    return render(request, 'article/create.html', context={})