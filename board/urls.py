from django.urls import path
from .views import BoardListView, ManagementListView

urlpatterns = [
    path('board/', BoardListView.as_view(), name='board'),
    path('management/', ManagementListView.as_view(), name='management'),

]
