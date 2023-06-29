from django.shortcuts import render
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    all_data = Task.objects.all()
    context = {
        "all_data": all_data,
    }

    return render(request, 'index.html', context=context)

def add_index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()

    return render(request, 'index.html',form=form)            



