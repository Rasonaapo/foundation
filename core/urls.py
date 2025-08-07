from django.urls import path
from .views import HomePageView, DashboardView, EventDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('events/<slug:slug>/', EventDetailView.as_view(), name='event_detail'),

]

