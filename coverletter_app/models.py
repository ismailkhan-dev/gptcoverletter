from django.db import models


# Create your models here.
class CoverLetter(models.Model):
    full_name = models.CharField(max_length=200)
    job_description = models.TextField()
    user_details = models.TextField()
    generated_cover_letter = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
