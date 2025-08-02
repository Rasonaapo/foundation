from .models import Footer

def footer_data(request):
    """
    Context processor to add footer data to the context.
    """
    footer = Footer.objects.first()
    return {
        'footer': footer
    }