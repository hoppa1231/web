from django.shortcuts import render
from .models import Product, Lessons, Groups


def reg(request):
    return render(request, 'main/index.html')


def main(request):
    array = Product.objects.all()
    lessons = Lessons.objects.all()
    groups = Groups.objects.all()
    return render(request, 'main/main.html', {'array': array, 'lessons': lessons, 'groups': groups, 'select': 'Products'})
