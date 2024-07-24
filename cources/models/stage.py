from shared.models import BaseModel
from cources.models.lessons import Lesson

from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models

class Stage(BaseModel):
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE)
    content = RichTextUploadingField()
    order = models.BigIntegerField()


class StageFile(BaseModel):
    file = models.FileField()
    stage = models.ForeignKey(Stage, 
                              on_delete=models.CASCADE)


class StageVideo(BaseModel):
    video = models.FileField()
    stage = models.ForeignKey(Stage, 
                              on_delete=models.CASCADE)
    

