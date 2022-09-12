from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#/manage.py shell_plus --print-sql

class Books(models.Model):

    Create = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Author = models.CharField(max_length=255)
    Title = models.CharField(max_length=255, null=True)
    Content = models.TextField(blank=True, null=True)
    Shop = models.CharField(max_length=255, null=True)
    Order = models.CharField(max_length=255, null=True)
    Price = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    Discount = models.CharField(max_length=255, null=True)
    Final_Price = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    Status = models.CharField(max_length=255, null=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.Create} - {self.Author} - {self.Title}'
        #return str(self.Create)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})