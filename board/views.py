from django.views.generic import ListView
from .models import Director

class BoardListView(ListView):
    model = Director
    template_name = 'board/board.html'
    context_object_name = 'directors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Trustees'
        # query for all trustee members where order is not 1 and team_type is trustee
        context['trustee_members'] = Director.objects.filter(team_type='trustee').exclude(order='1')
        # query for the trustee member with order 1
        context['trustee_ceo'] = Director.objects.filter(team_type='trustee', order='1').first()
        return context

class ManagementListView(ListView):
    model = Director
    template_name = 'board/management.html'
    context_object_name = 'management_team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Management Team'
        return context