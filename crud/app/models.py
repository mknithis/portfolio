from django.db import models

# Create your models here.





class Details(models.Model):
    Name_Details= models.CharField(max_length=50)
    Mail_Details = models.CharField(max_length=20)
    Mobile_Details = models.CharField(max_length=10,null=True)
    Age_Details=models.IntegerField(null=True)
    
    
    

    Job_Details = models.CharField(max_length=30)


def __str__(self):
    return self.Name_Details

