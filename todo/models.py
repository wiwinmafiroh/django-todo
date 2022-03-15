from django.db import models

# Create your models here.
class Todo(models.Model):
  # membuat field
  title = models.TextField(max_length=200)
  status = models.BooleanField(default=False)
  
  def __str__(self):
    # return yang ingin ditampilkan
    return self.title