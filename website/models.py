from django.db import models

class Modelos(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    description = models.TextField()
    instructions = models.TextField()
    predictor = models.FileField(upload_to='predictor')
    dataset = models.FileField(upload_to='dataset')


    def __str__(self):
        return self.title

