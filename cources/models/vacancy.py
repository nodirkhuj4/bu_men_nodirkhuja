from shared.models import BaseModel
from cources.models import category

from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


class Vacancy(BaseModel):
    title = models.CharField(max_length=64)
    category = models.ForeignKey(category.Category,
                                 on_delete=models.CASCADE)
    company_name = models.CharField(max_length=64)
    description = RichTextUploadingField()
    salary = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title