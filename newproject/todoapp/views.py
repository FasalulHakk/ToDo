from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Todo_form
from .models import tasks

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

class tasklv(ListView):
    model = tasks
    template_name = 'home.html'
    context_object_name = 'tasks'


class taskdv(DetailView):
    model = tasks
    template_name = 'details.html'
    context_object_name = 'obj'


class taskuv(UpdateView):
    model = tasks
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('task', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('abcdetail', kwargs={'pk': self.object.id})


class taskdeletv(DeleteView):
    model = tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('abchome')


def todo(request):
    obj = tasks.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        prty = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        usr = tasks(task=name, priority=prty, date=date)
        usr.save()
    return render(request, 'home.html', {'tasks': obj})


def delete(request, task_id):
    obj2 = tasks.objects.get(id=task_id)
    if request.method == 'POST':
        obj2.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    obj3 = tasks.objects.get(id=id)
    form = Todo_form(request.POST or None, instance=obj3)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'obj': obj3})
