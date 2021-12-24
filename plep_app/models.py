from django.db import models
import uuid



class Client(models.Model):
    PROJECT_CATG = (
        ('Web Project', 'Web Project'),
        ('Mobile App Dev Project', 'Mobile App Dev Project'),
        ('Machine Learning Project', 'Machine Learning Project'),
        ('Project', 'Project'),
    )
    uid = models.UUIDField(max_length=100, default=uuid.uuid4, primary_key=True)
    fullname = models.CharField(max_length=200, blank=True)
    superv_name = models.CharField(max_length=200, blank=True)
    project_catg = models.CharField(max_length=200, blank=True, choices=PROJECT_CATG)
    project_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    individual = models.BooleanField(default=False)
    grouped = models.BooleanField(default=False)
    member = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return str(self.fullname).title()

