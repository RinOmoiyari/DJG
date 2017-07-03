from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . import models, forms
import tasks

# Create your views here.
def deliverable_list(request):
    subheader = 'Deliverables'
    deliverables = models.Deliverable.objects.all()
    return render(request, 'deliverables/deliverable_list.html', {'deliverables':deliverables, 'subheader':subheader})

def deliverable_details(request, pk):
    deliverable = get_object_or_404(models.Deliverable, pk=pk)
    subheader = 'Deliverable %s' % (deliverable.pk)

    filtered_tasks = tasks.models.Task.objects.filter(related_deliv=pk)

    return render(request, 'deliverables/deliverable_details.html', {'deliverable':deliverable, 'subheader':subheader, 'tasks':filtered_tasks})

def deliverable_new(request):
    subheader = 'Create a New Deliverable'
    if request.method == "POST":
        form = forms.DeliverableForm(request.POST)

        if form.is_valid():
            deliverable = form.save(commit=False)
            deliverable.author = request.user
            deliverable.save()


            return redirect('deliverable_details', pk=deliverable.pk)

    else:
        form = forms.DeliverableForm()
        return render(request, 'deliverables/deliverable_edit.html', {'form':form, 'subheader':subheader})

def deliverable_edit(request, pk):
    deliverable = get_object_or_404(models.Deliverable, pk=pk)
    subheader = 'Edit: Deliverable %s' % (deliverable.pk)
    if request.method == "POST":
        form = forms.DeliverableForm(request.POST, instance=deliverable)
        if form.is_valid():
            deliverable = form.save(commit=False)
            deliverable.author = request.user
            deliverable.save()


            return redirect('deliverable_detail', pk=deliverable.pk)

    else:
        form = forms.DeliverableForm(instance=post)
        return render(request, 'deliverables/deliverable_edit.html', {'form':form, 'subheader':subheader})
