
#!Django modules and functions
from django.db import models
from django.utils.text import slugify



#!Python modules and functions
import uuid


#!Models and Serializers
from author.models import Author



# Create your models here.


#*Book
class Book(models.Model):
    book_id = models.UUIDField(('book id'),max_length=15,primary_key=True,unique=True,db_index=True,blank=True)
    language = models.CharField(('language'),max_length=50)
    book_title = models.CharField(('book title'),max_length=50)
    summary=models.TextField(('summary'),max_length=500,null=True,blank=True,help_text="Summary about the book")
    book_author = models.ManyToManyField(Author,related_name='bookauthor')
    book_pages = models.PositiveIntegerField(default=0)    
    book_slug = models.SlugField(('book slug'),unique=True,db_index=True,blank=True)
    # book_image = models.ImageField(_('book image'),upload_to='book/',validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    in_stock = models.BooleanField(('in_stock'),default=False)
    available_copies = models.IntegerField(('available_copies'),default=0)


    def __str__(self):
        return "{} ({})".format(self.book_title,self.language)
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
    def save(self, *args, **kwargs):
        self.book_slug = slugify(f"{self.book_title}")
        self.book_id = uuid.uuid4()
        super(Book,self).save(*args,**kwargs)
