from django.db import models

# Create your models here.
class Authors(models.Model):
    author_name=models.CharField(max_length=100)
    Born=models.CharField(max_length=50,default="No data available")
    About=models.CharField(max_length=500,default="No data Available")

    def __str__(self):
        return self.author_name

# Create your models here.
class Books(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author_name=models.ManyToManyField(Authors,related_name="maps")
    price=models.IntegerField()
    pub_year=models.IntegerField()
    summary=models.CharField(max_length=500)
    def __str__(self):
        return self.book_name
