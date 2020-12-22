from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


class Movie(models.Model):
    """
    Class to store movie information
    """
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Movie name', null=False, blank=False)
    rows = models.PositiveSmallIntegerField(default=100, verbose_name="Number of rows")
    columns = models.PositiveSmallIntegerField(default=100, verbose_name="Number of columns")


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        # movie = models.ForeignKey(Movie, null=False, on_delete=models.CASCADE)
        fields = ['name', 'rows', 'columns']

TICKET_STATUS_CHOICES = (
    (1, 'AVAILABLE'),
    (2, 'BLOCKED'),
    (3, 'BOOKED')
)


class Tickets(models.Model):
    """
    Class to store movie tickets information
    """
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    row_num = models.PositiveSmallIntegerField(null=False, blank=False)
    col_num = models.PositiveSmallIntegerField(null=False, blank=False)
    movie = models.ForeignKey(Movie, null=False, on_delete= models.CASCADE)
    status = models.IntegerField(choices=TICKET_STATUS_CHOICES, default=1)
    session = models.CharField(blank=False, null=False, max_length=200)

    class Meta:
        unique_together = ('movie', 'row_num', 'col_num')


class TicketsForm(ModelForm):
    class Meta:
        model = Tickets
        # ticket = models.ForeignKey(Tickets, null=False, on_delete=models.CASCADE)
        fields = ['row_num', 'col_num',]


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, default='0')
    desc = models.CharField(max_length=500)
