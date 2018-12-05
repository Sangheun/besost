from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.title

class Instructor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    id_photo = models.ImageField()

    def __str__(self):
        return self.name

class Slope(models.Model):
    slope_name = models.CharField(max_length=200)
    slope_description = models.TextField()
    slope_image = models.ImageField()

    def __str__(self):
        return self.slope_name

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_description = models.TextField()
    course_image = models.ImageField()

    def __str__(self):
        return self.course_name

class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question
