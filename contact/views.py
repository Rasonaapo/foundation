from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactMessageForm
from .models import ContactInfo

class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactMessageForm
    success_url = reverse_lazy('contact_success')  # Define success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch contact infos by type for display on right side
        infos = ContactInfo.objects.all()
        context['address_info'] = infos.filter(info_type='address').first()
        context['phone_info'] = infos.filter(info_type='phone').first()
        context['email_info'] = infos.filter(info_type='email').first()
        return context

    def form_valid(self, form):
        form.save()  # Save message to DB
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))