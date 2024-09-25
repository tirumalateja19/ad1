from django.db import models

# Create your models here.

class appointmentmodel(models.Model):
      name=models.CharField(max_length=100)
      email=models.EmailField()
      phoneno=models.IntegerField()
      category=models.TextField()
      date=models.DateField()
      message=models.TextField()

      def __str__(self):
        return self.name


