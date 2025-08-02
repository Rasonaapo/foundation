from django.views.generic import ListView
from .models import GalleryImage
from django.utils import timezone

class GalleryListView(ListView):
    model = GalleryImage
    template_name = 'media_gallery/gallery.html'
    context_object_name = 'images'

    def get_queryset(self):
        today = timezone.now().date()
        return GalleryImage.objects.filter(
            expires_at__isnull=True
        ) | GalleryImage.objects.filter(
            expires_at__gte=today
        )
