from django.urls import path
from bboard.views import index

from .views import index, by_rubric, BbCreateView, BbDetailView

urlpatterns = [
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]
