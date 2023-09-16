from django.db import models

# Create your models here.
class College(models.Model):
  col_name = models.CharField(max_length=50)

  def __str__(self):
    return self.col_name

class Participant(models.Model):
  num = models.AutoField(primary_key=True)
  student_num = models.CharField(max_length=20)
  fullname = models.CharField(max_length=100)
  year = models.PositiveSmallIntegerField()
  college = models.ForeignKey(College, on_delete=models.CASCADE)
  course = models.CharField(max_length=50)
  major = models.CharField(max_length=50)