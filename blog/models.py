from django.db import models

class blog(models.Model):
    title=models.CharField(max_length=240)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
