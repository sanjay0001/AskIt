from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=1000)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.question
class Answer(models.Model):
    answer = models.CharField(max_length=5000)
    like = models.IntegerField()
    dislike = models.IntegerField()
    forquestion = models.ForeignKey('Question', default=None, on_delete=models.CASCADE)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.answer

