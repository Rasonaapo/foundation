from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Type your message here',
            'rows': 6
        }),
    )
    subject = forms.CharField(
        max_length=100,
        label="Subject",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
    )
