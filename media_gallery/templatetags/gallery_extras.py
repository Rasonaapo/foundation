from django import template

register = template.Library()

@register.filter
def gallery_rows(images):
    """
    Chunk images into alternating [3,2,3,2,...] groups
    """
    result = []
    i = 0
    alt = True  # Start with 3
    while i < len(images):
        n = 3 if alt else 2
        result.append(images[i:i+n])
        i += n
        alt = not alt
    return result
