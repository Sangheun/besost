from django.contrib import admin

from .models import Post, Instructor, Slope, Course, Faq

# Register your models here.

admin.site.register(Post)
admin.site.register(Instructor)
admin.site.register(Slope)
admin.site.register(Course)
admin.site.register(Faq)

