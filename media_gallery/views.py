from django.views.generic import ListView
from .models import GalleryImage
from django.utils import timezone
from django.db.models import Q

class GalleryListView(ListView):
    model = GalleryImage
    template_name = 'media_gallery/gallery.html'
    context_object_name = 'images'

    def get_queryset(self):
        today = timezone.now().date()
        return GalleryImage.objects.filter(
            archived=False,
        ).filter(
            Q(expires_at__isnull=True) | Q(expires_at__gte=today)
        )

