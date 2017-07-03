from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . import models, forms
import deliverables

# Create your views here.
def task_list(request):
    subheader = 'Tasks'
    tasks = models.Task.objects.all()

    return render(request, 'tasks/task_list.html', {'tasks':tasks, 'subheader':subheader})

def task_details(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    subheader = 'Task %s' % (task.pk)
    return render(request, 'tasks/task_details.html', {'task':task, 'subheader':subheader})

def task_new(request, deliv_id=None):
    subheader = 'Create a New Task'
    if request.method == "POST":
        form = forms.TaskForm(request.POST)


        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()

            return redirect('task_details', pk=task.pk)

    else:
        form = forms.TaskForm(initial={'related_deliv': deliv_id})

        #if deliv_id:
        #    deliverable = deliverables.models.Deliverable.objects.filter(pk=deliv_id)
        #    form.fields["related_deliv"].queryset = deliverable

        return render(request, 'tasks/task_edit.html', {'form':form, 'subheader':subheader})

def task_edit(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    subheader = 'Edit: Task %s' % (task.pk)
    if request.method == "POST":
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()


            return redirect('task_details', pk=task.pk)

    else:
        form = forms.TaskForm(instance=task)
        return render(request, 'tasks/task_edit.html', {'form':form, 'subheader':subheader})
