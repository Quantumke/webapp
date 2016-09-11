from django.db import models
from markdown import markdown
from datetime import datetime, timedelta


# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    description=models.TextField(blank=True)

    class Meta:
        ordering=['title']
        verbose_name_plural='categories'

    def __unicode__(self):
        return  self.title
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug

class scales(models.Model):
    scale_name=models.CharField(max_length=100, unique=False)
    scale_details=models.TextField(max_length=3000)
    scale_document_url=models.URLField(max_length=100)
    scale_image=models.ImageField(upload_to='images', verbose_name='Image', blank=False)
    slug=models.SlugField(max_length=100, unique=True)
    category=models.ManyToManyField(Category)

    def save(self, force_insert=False, force_update=False):
        self.scale_details = markdown(self.scale_details)
        if self.scale_details:
            self.scale_details = markdown(self.scale_details)
        super(scales, self).save(force_insert, force_update)

    class Meta:
        ordering=['scale_name']
        verbose_name_plural='scales'
    def __unicode__(self):
        return  self.scale_name
    def __str__(self):
        return self.scale_name

    def get_absolute_url(self):
        return (self.slug)

class Contact(models.Model):
    name=models.CharField(max_length=100, unique=False)
    email=models.CharField(max_length=100, unique=False)
    subject=models.CharField(max_length=100, unique=False)
    message=models.TextField(blank=False)
    date=models.DateField(default=datetime.now(), blank=False)
    class Meta:
        ordering=['-date']
        verbose_name_plural='contacts'
    def __str__(self):
        return self.name
