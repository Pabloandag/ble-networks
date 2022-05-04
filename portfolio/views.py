from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Project

class HomeView(TemplateView):

    template_name = "portfolio/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context