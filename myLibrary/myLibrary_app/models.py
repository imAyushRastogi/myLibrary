from django.db import models



# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id=models.CharField(max_length=200)
    reader_name=models.CharField(max_length=200)
    reader_contact=models.IntegerField()
    reader_address=models.TextField()
    active=models.BooleanField(default=True)

class book(models.Model):
    def __str__(self):
        return self.book_name
    isbn_number=models.CharField(max_length=200)
    book_name=models.CharField(max_length=200)
    book_author=models.CharField(max_length=200)
    book_price=models.IntegerField()
    book_quntity=models.IntegerField()

