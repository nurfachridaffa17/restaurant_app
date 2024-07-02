from django.db import models
from django.utils.text import slugify

# Create your models here.
class Meals(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='meals/', null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

    def __str__(self):
        return self.name