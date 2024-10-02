from django.db import models


# Create your models here.
class File(models.Model):
    excel_file = models.FileField(upload_to='uploads/')
    files = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.excel_file.name
      


      
      
class InfoModel(models.Model):
    grade = models.CharField(max_length=100, null=True, default=None)
    class_name = models.CharField(max_length=100, null=True, default=None)
    number = models.CharField(max_length=100, null=True, default=None)
    name = models.CharField(max_length=100, null=True, default=None)
    sex = models.CharField(max_length=10)
    attitude = models.CharField(max_length=100, null=True, default=None)
    skill = models.CharField(max_length=100, null=True, default=None)
    friendship = models.CharField(max_length=100, null=True, default=None)
    minusclass = models.CharField(max_length=100, null=True, default=None)
    minusname = models.CharField(max_length=100, null=True, default=None)
    plusclass = models.CharField(max_length=100, null=True, default=None)
    plusname = models.CharField(max_length=100, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    