from django.db import models
from django.urls import reverse

# Create your models here.


class Centers(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='center', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'center'
        verbose_name_plural = 'centers'

    def get_url(self):
        return reverse('donationapp:districts_by_center', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class District(models.Model):
    objects = None
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    center = models.ForeignKey(Centers, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='district', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def get_url(self):
        return reverse('donationapp:distCendetail', args=[self.center.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)


