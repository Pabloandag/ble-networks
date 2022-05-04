from django.db import models
from datetime import date
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images")
    url = models.URLField(blank=True)
    date = models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.name