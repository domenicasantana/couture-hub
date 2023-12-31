from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Article, Comment
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView




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
                return redirect(reverse('blog:list'))
            
            queries = Q(title__icontains=query) | Q(body__icontains=query)
            articles = articles.filter(queries)

            # Check if articles queryset is empty
        if not articles:
            messages.info(request, "Your search didn't return any results.")
            return redirect(reverse('blog:list'))

    context = {
        'articles': articles,
        'search_term': query,
    }
    return render(request, "blog/article_list.html", context)


# View to display seleceted article
def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    total_likes = article.total_likes()
# In order to pass the liked to the frontend set it to false if the user has liked this article already
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        liked = True
    return render(request, 'blog/article_detail.html', {'article': article,
                                                            'total_likes': total_likes,
                                                            'liked': liked})


# View to create article, only allow this to logged in users
@login_required()
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article but don't commit to database
            instance = form.save(commit=False)
            # set the author field to the loggged in user
            instance.author = request.user
            instance.save()
            return redirect('blog:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'blog/article_create.html', {'form': form})


# View to like article, if the post is already liked, remove it
@login_required 
def LikeView(request, slug):
    post = get_object_or_404(Article, id=request.POST.get('article_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog:detail', args=[str(slug)]))


# View to add comment, only for logged in users
class AddCommentView(CreateView):
    model = Comment
    template_name = 'blog/add_comment.html'
    form_class = forms.CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article_slug = self.kwargs['slug']
        article = Article.objects.get(slug=self.kwargs['slug'])
        form.instance.post_id = article.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'slug': self.kwargs['slug']})


# View to update article, restricted for the creators of the article in the frontend
class UpdateArticleView(UpdateView):
    model = Article
    template_name = 'blog/article_edit.html'
    form_class = forms.ArticleForm

    def get_success_url(self):
        return reverse_lazy('blog:list')

# View to delete article, restricted for the creators of the article in the frontend
class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'

    def get_success_url(self):
        return reverse_lazy('blog:list')
