from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from django.views.generic import ListView, DetailView
from rubric.views import AllRubricMixin
from .forms import CommentForm
from django.shortcuts import redirect

from django.contrib import auth


class ListIndex(AllRubricMixin, ListView):
    model = Article
    template_name = 'articles/list.html'
    queryset = Article.objects.published()[:5]


class ArticleDetail(DetailView):
    template_name = 'articles/detail.html'
    # context_object_name = 'article_detail'  # or 'object' by default this name uses in forms
    model = Article

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        context['article_detail'] = self.get_object()
        context['comments_by_article'] = self.get_object().comments.all()
        return context


def add_comment_to_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            # comment = form.save(commit=False)
            comment.article = article
            comment.author = auth.get_user(request)
            comment.text = form.cleaned_data['comment_area']
            comment.save()
            return redirect('article-detail', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'articles/add_comment_to_article.html', {'form': form})
