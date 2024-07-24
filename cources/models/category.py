from shared.models import BaseModel

from django.db import models

class Category(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name