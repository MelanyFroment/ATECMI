from django.db import models

class Solution(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    benefits = models.TextField()
    process = models.TextField()
    use_cases = models.TextField()
    image = models.ImageField(upload_to='solutions/')

    def __str__(self):
        return self.title