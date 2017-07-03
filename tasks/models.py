from django.db import models
from django.utils import timezone
import deliverables
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=200)

    #work_type = models.CharField()
    #workflow = models.CharField()
    #workflow_phase = models.CharField

    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    requested_start_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    complete_date = models.DateTimeField(blank=True, null=True)
    related_deliv = models.ForeignKey('deliverables.Deliverable', blank=True, null=True)

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()


    def __str__(self):
        return self.title
