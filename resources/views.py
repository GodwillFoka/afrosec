from django.views.generic import ListView, DetailView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'resources/article_list.html'
    context_object_name = 'articles'
    paginate_by = 9

    def get_queryset(self):
        return Article.objects.filter(published=True)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'resources/article_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_articles'] = Article.objects.filter(published=True).exclude(id=self.object.id)[:3]
        return context
