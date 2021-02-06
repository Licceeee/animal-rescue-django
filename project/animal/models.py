from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from core.models import Timestamps  # noqa
from core.libs.core_libs import (get_headshot_image, get_image_format)  # noqa


# ---------------------------------------------------------------- >> FUNCTIONS
def img_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f'{instance.pk}.{ext}'
    else:
        # set filename as random string
        filename = f'{uuid4().hex}.{ext}'
    return (f'animal/{filename}')


def icon_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f'{instance.pk}.{ext}'
    else:
        filename = f'{uuid4().hex}.{ext}'
    return (f'icons/{filename}')


# ------------------------------------------------------------------ >> CLASSES
class AnimalGroup(Timestamps):
    """model for group of animals:
            mammals, birds, reptiles, amphibians, fish, invertebrates.
    """
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.name}"


class AnimalType(Timestamps):
    """model for _type of animal.
        e.g.: cat, dog, mouse, etc..
    """
    name = models.CharField(max_length=256, unique=True)
    group = models.ForeignKey(AnimalGroup, null=True, on_delete=models.PROTECT)
    icon = models.ImageField(default=None, upload_to=icon_dir_path,
                             null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def headshot_image(self):
        return get_headshot_image(self.icon, 100)
    headshot_image.short_description = _('Preview')

    def get_icon(self):
        return get_image_format(self.icon, 50)
    get_icon.short_description = _('Icon')


class AnimalCondition(Timestamps):
    """model for condition of animal.
        e.g.: injured, ill, malnourished, good shape, etc..
    """
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Animal(Timestamps):
    """model for condition of animal.
        e.g.: injured, ill, malnourished, good shape, etc..
    """
    _type = models.ForeignKey(AnimalType, on_delete=models.PROTECT)
    conditions = models.ManyToManyField(AnimalCondition)
    description = models.CharField(max_length=256, null=True, blank=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(default=None, upload_to=img_dir_path,
                              null=True, blank=True)

    def __str__(self):
        conditions = ", ".join([
            condition.name for condition in self.conditions.all()])
        return f"{self._type.name}: {conditions}"

    # TODO filter Animal by last 2 weeks

    def get_conditions(self):
        return ", ".join([
            condition.name for condition in self.conditions.all()])
    get_conditions.short_description = "Condition"

    def get_images(self):
        """returns nr of inline images"""
        if self.image:
            return self.animalimage_set.count() + 1
        return self.animalimage_set.count()
    get_images.short_description = _('# Images')

    def headshot_image(self):
        return get_headshot_image(self.image, 300)
    headshot_image.short_description = _('Preview')

    def get_image(self):
        return get_image_format(self.image, 100)
    get_image.short_description = _('Image')


class AnimalImage(models.Model):
    animal = models.ForeignKey(Animal, default=None,
                               on_delete=models.CASCADE)
    image = models.ImageField(default=None, upload_to=img_dir_path,
                              null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.animal._type.name}: {self.animal.name}")

    def get_image(self):
        return get_image_format(self.image, 100)

    get_image.short_description = _('Image')

    def headshot_image(self):
        return get_headshot_image(self.image, 300)
    headshot_image.short_description = _('Preview')

    def get_animal(self):
        return (f"{self.animal._type.name}: {self.animal.name}")
    get_animal.short_description = _('Animal')

    def get_post_date(self):
        return self.animal.created
    get_post_date.short_description = _('Date')
