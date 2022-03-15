from logging import exception
from django.shortcuts import render, reverse
# Import response nya
from django.http import HttpResponseRedirect
# Import django exception
from django.core.exceptions import ObjectDoesNotExist 
# Import models
from .models import Todo

# Create your views here.
def index(request):
  items = Todo.objects.order_by('-id')
  # 'items': items -> value yang ingin dibawa ke template (berupa dict)
  return render(request, 'todo/index.html', {'items': items})

def done(request):
  items = Todo.objects.filter(status=True).order_by('-id')
  return render(request, 'todo/index.html', {'items': items})

def pending(request):
  items = Todo.objects.filter(status=False).order_by('-id')
  return render(request, 'todo/index.html', {'items': items})

def delete_all(request):
  Todo.objects.all().delete()
  return HttpResponseRedirect(reverse('index'))

def create(request):
  try:
    # mengambil data form
    title = request.POST['title']
    todo = Todo(title=title)
    todo.save()
    print(title)
    return HttpResponseRedirect(reverse('index'))
  except exception:
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
  try:
    todo = Todo.objects.get(id=id)
    todo.status = not todo.status
    todo.save()
    return HttpResponseRedirect(reverse('index'))
  except ObjectDoesNotExist:
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  try:
    # ambil todo
    todo = Todo.objects.get(id=id)
    todo.delete()
    # ketika berhasil dihapus, maka akan direct ke halaman semula
    return HttpResponseRedirect(reverse('index'))
  except ObjectDoesNotExist:
    return HttpResponseRedirect(reverse('index'))
