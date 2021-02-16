from collections import Counter
from datetime import datetime
from operator import itemgetter

from django.db import models
from iteration_utilities import flatten, unique_everseen, duplicates

class Event(models.Model):
    source = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    className = models.CharField(max_length=500, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    startTime = models.CharField(max_length=20, null=True, blank=True)
    endTime = models.CharField(max_length=20, null=True, blank=True)
    startRecur = models.DateTimeField(null=True, blank=True)
    endRecur = models.DateTimeField(null=True, blank=True)
    allDay = models.BooleanField(null=True, blank=True)
    daysOfWeek = models.JSONField(default=list)
    url = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.source} - {self.title}'


class SourceArchive(models.Model):
    DOWNLOADING = 'downloading'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    FAILED = 'failed'
    STATUS = (
        (DOWNLOADING, DOWNLOADING),
        (PROCESSING, PROCESSING),
        (SUCCESS, SUCCESS),
        (FAILED, FAILED),
    )

    source = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=5000, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    status = models.TextField(max_length=100, choices=STATUS, default=PENDING, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.source} - {self.url} - {self.created}'
