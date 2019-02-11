from django.urls import path
from .views import ListIndex, ArticleDetail, add_comment_to_article

urlpatterns = [
    path('', ListIndex.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('<int:pk>/comment/', add_comment_to_article, name='add_comment_to_article'),
]
