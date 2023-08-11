
#!Django modules and functions
from django.db import models
from django.utils.text import slugify



#!Python modules and functions
import uuid


#!Models and Serializers
# Create your models here.


#*Author
class Author(models.Model):
    author_name = models.CharField(('name'),max_length=50,db_index=True,unique=True)
    author_surname = models.CharField(('surname'),max_length=50)
    author_slug = models.SlugField(('author_slug'),unique=True,db_index=True,blank=True)
    description = models.TextField(('description'),blank=True,null=True)
    birth_date = models.DateField(("birthdate"),null=True,blank=True)
    died_date = models.DateField(("died_date"),null=True,blank=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return "{}".format(self.author_name)

    def save(self,*args,**kwargs):
        self.author_slug = slugify(f"{self.author_name}-{self.author_surname}")
        super(Author,self).save(*args,**kwargs)