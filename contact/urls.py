from django.urls import path
from .views import ContactFormView
from django.views.generic import TemplateView

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='contact/contact_success.html'), name='contact_success'),

]
