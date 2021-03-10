from django.urls import path
from bboard.views import index

# from .views import index, by_rubric, BbCreateView, BbDetailView, BbByRubricView
from .views import BbCreateView, BbDetailView, BbByRubricView, BbEditView, BbDeleteView, BbIndexView, \
    BbMonthArchiveView, BbWeekArchiveView

urlpatterns = [
    path('<int:year>/week/<int:week>/', BbWeekArchiveView.as_view(date_field='published')),
    path('<int:year>/<int:month>/', BbMonthArchiveView.as_view()),
    # path('detail/<int:year>/<int:month>/<int:day>/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('', BbIndexView.as_view(), name='index'),
]
