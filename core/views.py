from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from media_gallery.models import MarqueeImage
from django.utils import timezone
from .models import Event, MostTrending, Category

class HomePageView(TemplateView):
    template_name = 'core/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marquee_images'] = MarqueeImage.objects.all()
        context['title'] = 'Jirajinapor Foundation'

        # Only show events that are NOT archived and have not expired
        context['events'] = Event.objects.filter(
            archived=False,
            expiry_date__gte=timezone.now().date()
        ).order_by('-event_date')[:5]
        context['most_trending'] = MostTrending.objects.order_by('-created_at')[:5]
        return context

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'core/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['most_trending'] = MostTrending.objects.order_by('-created_at')[:5]
        return context

