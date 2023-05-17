from django.db import models

class Articles(models.Model):
    title = models.CharField('Jobs_title', max_length=50)
    description = models.TextField('Job_description')
    budget = models.CharField('Budget', max_length=20)
    data = models.DateTimeField('Publishing_data')

    def __str__(self):
        return self.title


