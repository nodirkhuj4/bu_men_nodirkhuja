from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Settings(BaseModel):
    objects = models.Manager()
    email = models.EmailField()
    links = models.URLField()
    contact_phone = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.BigIntegerField()
    latitude = models.BigIntegerField()
    location_text = models.TextField(_('location_text'))

    class Meta:
        verbose_name = _('Settings')
        verbose_name_plural = _("Settings")
        db_table = 'settings'

    def __str__(self):
        return "Settings"


class News(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _("News")
        db_table = 'news'

    def __str__(self):
        return self.title


class Quotes(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _('Quotes')
        verbose_name_plural = _("Quotes")
        db_table = 'quotes'

    def __str__(self):
        return self.title


class Advertising(BaseModel):
    image = models.ImageField(upload_to='advertising/%Y/%m/')

    class Meta:
        verbose_name = _('Advertising')
        verbose_name_plural = _("Advertising")
        db_table = 'advertising'

    def __str__(self):
        return f"image {self.id}"


class FAQ(BaseModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _("FAQ")
        db_table = 'faq'

    def __str__(self):
        return self.question