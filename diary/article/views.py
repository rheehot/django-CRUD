from django.shortcuts import render, redirect, reverse
from article.models import Article

# Create your views here.
def index(request):
    queryset = Article.objects.all()
    context = {
        'articles': queryset,
    }
    return render(request, 'article/index.html', context=context)

def create(request):
    # GET 일때
    if request.method == 'GET':
        return render(request, 'article/create.html', context={})

    # POST 일때
    title = request.POST['title']
    content = request.POST['content']
    article = Article.objects.create(title=title, content=content)

    pk = article.id
    url = reverse('article:retrieve', kwargs={'pk': pk})
    return redirect(to=url)

def retrieve(request, pk):
    article = Article.objects.get(id=pk)

    context = {
        'article': article,
    }

    return render(request, 'article/retrieve.html', context=context)

def update(request, pk):
    article = Article.objects.get(id=pk)

    # GET 일때
    if request.method == 'GET':
        context = {
            'article': article
        }
        return render(request, 'article/update.html', context=context)

    # Request 에서 받아온 내용들
    title = request.POST['title']
    content = request.POST['content']

    # DB에 바꿀 내용들
    article.title = title
    article.content = content
    article.save()

    return redirect(to='/article/{}'.format(pk))

def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()

    return redirect(to='/')