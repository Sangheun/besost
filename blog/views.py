from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Instructor, Course, Slope, Faq

# Create your views here.
def index(request):
    course_list = Course.objects.all()
    faq_list = Faq.objects.all()
    post_list = Post.objects.all()
    context = {
        'course_list':course_list,
        'faq_list':faq_list,
        'post_list':post_list,
    }
    return render(request, 'blog/index.html', context=context)

def about(request):
    return render(request, 'blog/about.html')

def course(request):
    return render(request, 'blog/course.html')
