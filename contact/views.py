from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage

class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        # Save the message
        ContactMessage.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            message=form.cleaned_data['message'],
            subject = form.cleaned_data['subject']
        )

        messages.success(self.request, 'Your message has been sent successfully!')
        return super().form_valid(form)
