from django.db import models

class UserUploads(models.Model):
    location_name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images/')
    location_long_lat = models.CharField(max_length=225)
    summary_info = models.CharField(max_length=225)

    def __str__(self):
        return self.location_name