from django.db import models
from author.models import Author

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=100)
    #pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE , blank = False ,null = False)
    #Published, Withdrawn, Draft
    status_choices = ( 
    ('Draft', 'Draft'), 
    ('Withdrawn', 'Withdrawn'), 
    ('Published', 'Published'), 
    ) 
    status = models.CharField( max_length= 20,choices= status_choices,default= 'Draft',blank= False,null= False )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
