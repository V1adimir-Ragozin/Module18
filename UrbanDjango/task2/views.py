from django.shortcuts import render
from django.views.generic import TemplateView


def class_template(request):
    return render(request, 'class_template.html')


def func_template(request):
    return render(request, 'func_template.html')


def main_template(request):
    return render(request, 'main_template.html')


class ClassTemplate(TemplateView):
    template_name = 'class_template.html'


class FuncTemplate(TemplateView):
    template_name = 'func_template.html'


class MainTemplate(TemplateView):
    template_name = 'main_template.html'
