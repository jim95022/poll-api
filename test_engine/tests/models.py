from datetime import datetime
from django.db import models

TYPE_CHOICES = [('T', 'Text'), ('O', 'One'), ('M', 'Multiple')]


class Poll(models.Model):
    slug = models.SlugField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default='')
    description = models.TextField(blank=True)
    qstns = models.ManyToManyField('Questions',  blank=True, related_name='questions')

    class Meta:
        ordering = ['created']


    def __str__(self):
        return '{}'.format(self.slug)


class Questions(models.Model):
    poll_name = models.SlugField(max_length=150, null=True)
    body = models.TextField(blank=True)
    type_qstn = models.CharField(choices=TYPE_CHOICES, default='Text', max_length=100)
    Results = models.ManyToManyField('Results', blank=True, related_name='results')

    def __str__(self):
        return '{}'.format(self.poll_name)


class Results(models.Model):
    user = models.IntegerField()
    poll_name = models.SlugField(max_length=150, blank=True)
    result = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.user)


    