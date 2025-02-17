from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/') #Uploads to media/resumes/

    def __str__(self):
        return self.file.name
