from ckeditor_uploader.fields import RichTextUploadingField

from shared.models import BaseModel
from users.models import User

from django.db import models
from django.utils.translation import gettext_lazy as _


class Settings(BaseModel):
    objects = models.Manager()
    email = models.EmailField()
    links = models.URLField()
    contact_phone = models.CharField(max_length=30, null=True, blank=True)
    appstore_link = models.URLField(null=True, blank=True)
    playmarket_link = models.URLField(null=True, blank=True)
    longitude = models.BigIntegerField()
    latitude = models.BigIntegerField()
    location_text = models.TextField(_('location_text'))
    telegram = models.CharField(max_length=64, null=True, blank=True)
    instagram = models.CharField(max_length=64, null=True, blank=True)
    linkedin = models.CharField(max_length=64, null=True, blank=True)
    facebook = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = _('Settings')
        verbose_name_plural = _("Settings")

    def __str__(self):
        return "Settings"
    

class Page(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _("Page")


class News(BaseModel):
    title = models.CharField(max_length=255)
    banner = models.ImageField(upload_to="common/news/%Y/%m", null=True)
    content = RichTextUploadingField()
    slug = models.SlugField()
    top = models.BooleanField(default=False)
    view_count = models.PositiveBigIntegerField(default=0)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _("News")

    def __str__(self):
        return self.title


class Quotes(BaseModel):
    author = models.CharField(max_length=255)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _('Quotes')
        verbose_name_plural = _("Quotes")

    def __str__(self):
        return self.title


class Advertising(BaseModel):
    image = models.ImageField(upload_to='advertising/%Y/%m/')
    link = models.URLField(blank=True)

    class Meta:
        verbose_name = _('Advertising')
        verbose_name_plural = _("Advertising")

    def __str__(self):
        return f"image {self.id}"


class UserContactApplication(BaseModel):

    class SourceChoice(models.TextChoices):
        MOBILE = "MB", "MOBILE"
        LANDING = "LD", "LANDING"

    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE, 
                             null=True)
    
    email = models.EmailField(null=True)
    full_name= models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=25, null=True)
    message = models.TextField(max_length=500)
    file = models.FileField(upload_to="%Y/%M/", null=True)

    source = models.CharField(max_length=3, 
                              choices=SourceChoice.choices, default=SourceChoice.LANDING)
    
    is_contacted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.full_name
    

    class Meta:
        ordering = ['is_contacted', 'created_at']
        verbose_name = _("User Contact Application")
        verbose_name_plural = _("User Contact Application")


class AboutApp(BaseModel):
    caption = models.CharField(max_length=50)
    text = models.TextField()
    order = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("About App")
        verbose_name_plural = _("About App")

    def save(self, *args, **kwargs) -> None:
        self.order = 1
        last_about_app = AboutApp.objects.order_by('order').last()
        if last_about_app:
            order = last_about_app + 1
        self.order = order

        super.save(*args, **kwargs)


class FAQ(BaseModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = _('FAQ')
        verbose_name_plural = _("FAQ")

    def __str__(self):
        return self.question
    
class NewsView(BaseModel):
    news = models.ForeignKey(News, 
                             on_delete=models.CASCADE, 
                             blank=True, null=True)
    visitor = models.UUIDField()
    ip = models.GenericIPAddressField()
    

    def __str__(self) -> str:
        return f"{self.ip} -> {self.news.title}"