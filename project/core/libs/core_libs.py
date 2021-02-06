from django.utils.html import format_html
from datetime import datetime, date
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy, gettext_lazy as _



def get_headshot_image(image):
    """returns the image displayedin admin inlines overview"""
    if image:
        return format_html(f'<a href="{image.url}" target="_blank">'
                           f'<img src="{image.url}" style="max-width:800px;" />'
                           f'</a>')


def get_image_format(image):
    """returns the image displayed in admin model overview"""
    if image:
        return format_html(
            f'<img src="{image.url}" style="max-width:100px;" />')
    else:
        return _("No Image Found")
