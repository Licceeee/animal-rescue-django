from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


def get_headshot_image(image, size):
    """returns the image displayedin admin inlines overview"""
    if image:
        return format_html(f'<a href="{image.url}" target="_blank">'
                           f'<img src="{image.url}" style="height:{size}px;'
                           f'border-radius: 5px;'
                           f'box-shadow: 0px 2px 17px -4px #6D8291;"/> </a>')


def get_image_format(image, size):
    """returns the image displayed in admin model overview"""
    if image:
        return format_html(
            f'<img src="{image.url}" style="height:{size}px; '
            f'border-radius: 5px;'
            f'box-shadow: 0px 2px 17px -4px #6D8291;"/>')
    else:
        return _("No Image Found")
