from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['message', 'name', 'email', 'subject']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('message', css_class='form-control'),
            Row(
                Column('name', css_class='form-control col-sm-6 pr-1'),
                Column('email', css_class='form-control col-sm-6 pl-1'),
            ),
            Field('subject', css_class='form-control'),
            Submit('submit', 'Send Message', css_class='btn btn-primary mt-3')
        )
        
        # Add 'is-invalid' class to fields with errors
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                existing_classes = field.widget.attrs.get('class', '')
                if 'is-invalid' not in existing_classes:
                    field.widget.attrs['class'] = (existing_classes + ' is-invalid').strip()