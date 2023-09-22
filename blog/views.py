from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Article, Comment
from django.db.models import Q



# View to list all existing articles and order them by date
def article_list(request):
    articles = Article.objects.all().order_by("date")
    query = None
    categories = None
    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category']
            articles = articles.filter(category__name__in=categories)
            categories = Cate

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('articles:list'))
            
            queries = Q(title__icontains=query) | Q(body__icontains=query)
            articles = articles.filter(queries)

    context = {
        'articles': articles,
        'search_term': query,
    }
    return render(request, "blog/article_list.html", context)

