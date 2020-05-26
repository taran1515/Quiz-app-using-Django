from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


