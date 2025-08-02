from django.views.generic import ListView
from .models import Director

class BoardListView(ListView):
    model = Director
    template_name = 'board/board.html'
    context_object_name = 'directors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Board of Directors'
        return context

