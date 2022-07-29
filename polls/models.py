from django.db import models

# Create your models here. - ORM: Object Relational Mapper


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data_published')

    def __str__(self):
        return self.question_text

