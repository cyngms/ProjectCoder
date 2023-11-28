from django.shortcuts import render
from .models import Course


# Create your views here.


def show_courses(request):
    courses = Course.object.all()

    context = {
        'Course': courses,
        'name': 'Cynthia',
        'title': 'Courses',
    }

    return render(request, 'AppCoder/courses.html', context)
