# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
# Create your views here.
def index(request):
    entries = Entry.objects.order_by('-date_posted') # Or can have .all()

    context = {'entries' : entries}
    return render(request, 'daily/index.html', context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('daily:index')
    else:
        form = EntryForm()


    context = {'form': form}
    return render(request, 'daily/add.html', context)
