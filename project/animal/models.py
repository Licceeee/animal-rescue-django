from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from core.models import Timestamps  # noqa
from core.libs.core_libs import (get_headshot_image, get_image_format)  # noqa
from location_field.models.plain import PlainLocationField


# ---------------------------------------------------------------- >> FUNCTIONS
def img_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f'{instance.pk}.{ext}'
    else:
        # set filename as random string
        filename = f'{uuid4().hex}.{ext}'
    return (f'animals/{filename}')


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
    """model for animal_type of animal.
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

    def get_animal_numbers(self):
        return self.animal_set.count()
    get_animal_numbers.short_description = _('# Animals')


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

    ANIMAL_STATE = (
        ('F', _("Found")),
        ('M', _("Missing"))
    )

    GENDER = (
        ('F', _("Female")),
        ('M', _("Male")),
        ('U', _("Unknown"))
    )

    # AGE = (
    #     ('B', _("Baby")),
    #     ('A', _("Adult")),
    #     ('U', _("Uncertain")),
    # )

    post_type = models.CharField(max_length=2, choices=ANIMAL_STATE,
                                 default='F')
    animal_type = models.ForeignKey(AnimalType, on_delete=models.PROTECT,
                                    null=True, blank=True,
                                    related_name='animal_type_ordered')
    conditions = models.ManyToManyField(AnimalCondition)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(default=None, upload_to=img_dir_path,
                              null=True, blank=True)
    is_chipped = models.BooleanField(default=False)
    chip = models.CharField(max_length=256, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='U')
    age_years = models.IntegerField(default=0)
    age_months = models.IntegerField(default=0)
    neutered = models.BooleanField(default=False)
    location = PlainLocationField(based_fields=['city'], zoom=7,
                                  null=True, blank=True)

    def __str__(self):
        conditions = ", ".join([
            condition.name for condition in self.conditions.all()])
        return f"{self.animal_type}: {conditions}"

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
        if self.image:
            return get_image_format(self.image, 100)
        else:
            return "No Image"
    get_image.short_description = _('Image')


class AnimalImage(models.Model):
    animal = models.ForeignKey(Animal, default=None,
                               on_delete=models.CASCADE)
    image = models.ImageField(default=None, upload_to=img_dir_path,
                              null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.animal.animal_type.name}: {self.animal.name}")

    def get_image(self):
        return get_image_format(self.image, 100)

    get_image.short_description = _('Image')

    def headshot_image(self):
        return get_headshot_image(self.image, 300)
    headshot_image.short_description = _('Preview')

    def get_animal(self):
        return (f"{self.animal.animal_type.name}: {self.animal.name}")
    get_animal.short_description = _('Animal')

    def get_post_date(self):
        return self.animal.created
    get_post_date.short_description = _('Date')
