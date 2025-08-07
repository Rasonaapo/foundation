from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div, Row, Column

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'name', 'email', 'website']
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Write Comment',
                'rows': 9,
                'class': 'form-control w-100',
                'id': 'comment',
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-control',
                'id': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control',
                'id': 'email',
            }),
            'website': forms.URLInput(attrs={
                'placeholder': 'Website',
                'class': 'form-control',
                'id': 'website',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('body', css_class='form-control w-100', placeholder='Write Comment', rows=9),
            Row(
                Column(Field('name', css_class='form-control', placeholder='Name'), css_class='col-sm-6 pr-1'),
                Column(Field('email', css_class='form-control', placeholder='Email'), css_class='col-sm-6 pl-1'),
                css_class='form-row'
            ),
            Field('website', css_class='form-control w-100 mt-2', placeholder='Website'),
        )

