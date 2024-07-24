from shared.models import BaseModel
from cources.models.stage import Stage
from users.models import User

from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models

class TestQuestion(BaseModel):
    stage = models.ForeignKey(Stage,
                              on_delete=models.CASCADE)
    text = RichTextUploadingField()

    
class UserTestAnswer(BaseModel):
    question = models.ForeignKey(TestQuestion,
                                 on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    

class UserTestResult(BaseModel):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage,
                              on_delete=models.CASCADE)
    questions = models.PositiveIntegerField()
    correct_answer_count = models.PositiveIntegerField()
    correct_precent = models.PositiveIntegerField()
    started_at = models.DateTimeField()
    finished_at =  models.DateTimeField()


class TestQuestionChoice(BaseModel):
    question = models.ForeignKey(TestQuestion,
                                 on_delete=models.CASCADE)
    
    text = RichTextUploadingField()
    is_correct = models.ForeignKey(UserTestAnswer,
                                   on_delete=models.CASCADE)
    