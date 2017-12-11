from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, max_length=10)
    category_title = models.CharField(max_length=250)

    def __str__(self):
        return self.category_title


class Author(models.Model):
    author_id = models.AutoField(primary_key=True, max_length=10)
    author_name = models.CharField(max_length=250)

    def __str__(self):
        return self.author_name


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True, max_length=10)
    publisher_name = models.CharField(max_length=250)

    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True, max_length=10)
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=250)
    book_sub_title = models.CharField(max_length=250)
    book_description = models.TextField(null=True, blank=True)
    book_ISBN = models.CharField(max_length=250)
    book_pages = models.CharField(max_length=250)
    book_year = models.CharField(max_length=250)
    book_cover = models.FileField(upload_to='books/cover/', max_length=250)
    book_pdf = models.FileField(upload_to='books/pdf/', max_length=250)

    def __str__(self):
        return self.book_title
