from django.db import models

# Create your models here.
class Books(models.Model):
    bname=models.CharField(max_length=200)
    prize=models.PositiveIntegerField()
    Date=models.CharField(max_length=200)
    author=models.CharField(max_length=200) 
    profile_pic=models.ImageField(upload_to="images",null=True)


    def __str__(self):
        return self.bname
    