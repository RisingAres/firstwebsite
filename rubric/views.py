from articles.models import Rubric, Article
from django.views.generic import ListView, DeleteView


class AllRubricMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class RubricIndex(AllRubricMixin, ListView):
    model = Rubric
    template_name = 'rubric/rubric_list.html'


class RubricDetail(DeleteView):
    model = Rubric
    template_name = 'rubric/rubric_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RubricDetail, self).get_context_data(*args, **kwargs)
        context['rubrics'] = self.get_queryset()
        context['rubric'] = self.get_object()
        context['article_from_rubric'] = self.get_object().articles.all()
        return context
