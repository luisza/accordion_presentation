from django.shortcuts import render
from .models import PresentationModel

# Create your views here.


class PresentationUpdate(UpdateView):
    model = PresentationModel
