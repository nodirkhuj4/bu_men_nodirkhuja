from shared.models import BaseModel
from cources.models.lessons import Lesson

from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models

class Club(BaseModel):
    theme = models.OneToOneField(Lesson, 
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.title
    

class ClubPost(BaseModel):
    club = models.ForeignKey(Club, 
                             on_delete=models.CASCADE)
    content = RichTextUploadingField()

    def __str__(self) -> str:
        return self.club.title