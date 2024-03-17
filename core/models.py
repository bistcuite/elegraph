import tinymce.models as tinymce_models
from django.dispatch import receiver
from django.db import models
from .slugify import unique_slug_generator

class Post(models.Model):
    slug = models.SlugField(null=False,verbose_name="آدرس")
    title = models.CharField(max_length=250,verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوای پست")
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست‌ها'
    
@receiver(models.signals.pre_save, sender=Post)
def auto_slug_generator(sender, instance, **kwargs):
    """
    Creates a slug if there is no slug.
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)