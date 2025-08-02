from django.views.generic import TemplateView, ListView
from .models import Mission, Vision, Value, Introduction


class AboutPageView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['introduction'] = Introduction.objects.first()
        context['mission'] = Mission.objects.first()
        context['vision'] = Vision.objects.first()
        context['values'] = Value.objects.all()
        context['title'] = "About Us"
        return context