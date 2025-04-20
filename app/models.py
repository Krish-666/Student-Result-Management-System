from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class result(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE) # dont know this query
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"