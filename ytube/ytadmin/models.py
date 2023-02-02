from django.db import models

# Create your models here.
class Ytsave:
    file = models.FileField(upload_to = 'student/')