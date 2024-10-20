from django.shortcuts import render
from .models import Sala
import json

def get_one(request):
  id = request.GET.get('id')
  Sala.objects.get(id=id)
  return json.dumps(Sala.objects.get(id=id))
  