from django.shortcuts import render


def welcome(request):
    return render("Hi", 'AppCoder/courses.html')
