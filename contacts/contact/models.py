from django.db import models
from rest_framework import serializers
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone = models.CharField(max_length=50)
  email = models.EmailField(max_length=50, blank=True)
  created_date = models.DateTimeField(default=timezone.now())
  description = models.TextField(blank=True)
  
  def __str__(self):
    return f'{self.first_name} {self.last_name}'
  
class Category(models.Model):
  class Meta:
    verbose_name: "Categoria"
    verbose_plural_name: "Categorias"
    
  name = models.CharField(max_length=50)
    
class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ('first_name', 'last_name', 'phone', 'email', 'description')
  
