import uuid
import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def resize_image(image_field, max_width=1200, max_height=800):
    img = Image.open(image_field)
    img = img.convert('RGB')
    img.thumbnail((max_width, max_height), Image.LANCZOS)

    thumb_io = BytesIO()
    img.save(thumb_io, format='JPEG', quality=85)

    # Generate a new unique filename
    ext = 'jpg'  
    unique_name = f"{uuid.uuid4().hex}.{ext}"

    new_image = ContentFile(thumb_io.getvalue(), name=unique_name)
    return new_image
