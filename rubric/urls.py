from django.urls import path
from .views import RubricIndex, RubricDetail

urlpatterns = [
    # path('', RubricIndex.as_view(), name='rubric-list'),
    path('<int:pk>/', RubricDetail.as_view(), name='rubric-detail')
]
