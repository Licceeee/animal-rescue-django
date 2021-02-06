from django.db import models
from django.utils.translation import ugettext_lazy, gettext_lazy as _
from uuid import uuid4

from core.libs.core_libs import (get_headshot_image, get_image_format)


# ----------------------------------------------------------------- >> FUNCTIONS
def img_dir_path(instance, filename,):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f'{instance.pk}.{ext}'
    else:
        # set filename as random string
        filename = f'{uuid4().hex}.{ext}'
    return (f'animals/{filename}')


# ------------------------------------------------------------------- >> CLASSES
class AnimalType(models.Model):
    """model for type of animal. 
        e.g.: cat, dog, mouse, etc..
    """
    name = models.CharField(max_length=256, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class AnimalCondition(models.Model):
    """model for condition of animal. 
        e.g.: injured, ill, malnourished, good shape, etc..
    """
    name = models.CharField(max_length=256, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Animal(models.Model):
    """model for condition of animal. 
        e.g.: injured, ill, malnourished, good shape, etc..
    """
    type = models.ForeignKey(AnimalType, on_delete=models.PROTECT)
    conditions = models.ManyToManyField(AnimalCondition)
    name = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(default=None, upload_to=img_dir_path,
                              null=True, blank=True)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        conditions = ", ".join([
            condition.name for condition in self.conditions.all()])
        return f"{self.type.name}: {conditions}"

    def get_conditions(self):
        return ", ".join([
            condition.name for condition in self.conditions.all()])
    get_conditions.short_description = "Condition"

    # def get_images(self):
    #     """returns nr of inline images"""
    #     if self.image:
    #         return self.postimage_set.count() + 1
    #     return self.postimage_set.count()
    # get_images.short_description = _('# Images')

    def headshot_image(self):
        return get_headshot_image(self.image)
    headshot_image.short_description = _('Preview')

    def get_image(self):
        return get_image_format(self.image)
    get_image.short_description = _('Image')





