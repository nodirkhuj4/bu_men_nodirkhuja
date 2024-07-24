from shared.models import BaseModel
from cources.models import category

from django.db import models

class LessonTheme(BaseModel):
    title = models.CharField(max_length=64)
    photo = models.ImageField(upload_to="lesson/%Y/%m")
    author_name = models.CharField(max_length=64)
    category = models.ForeignKey(category.Category, 
                                 on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.title
    


class Lesson(BaseModel):

    class LessonType(models.TextChoices):
        LOCAL = 'LC', 'LOCAL'
        INTERNATIONAL = 'IN', 'INTERNATIONAL'

    type = models.CharField(max_length=2,
                            choices=LessonType.choices)
    theme = models.ForeignKey(LessonTheme,
                              on_delete=models.CASCADE)
    
    
