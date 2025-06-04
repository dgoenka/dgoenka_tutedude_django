from django.db import models
import datetime
from ckeditor.fields import RichTextField  # For CKEditor


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    content = models.TextField(max_length=10000, null=False, blank=False)

class Post(models.Model):
        title = models.CharField(max_length=200, null=False, blank=False)
        public_date = models.DateTimeField(auto_now_add=True)
        image = models.ImageField(upload_to='images/')
        body = RichTextField(max_length=10000, null=False, blank=False)

        def summary(self):
            return (self.body or "")[:100]

        def pub_date(self):
            return (self.public_date or datetime.datetime.now()).strftime("%B %d, %Y")

        def __str__(self):
            return self.title

