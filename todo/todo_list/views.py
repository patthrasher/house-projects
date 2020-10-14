from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def room(request) :
    return render(request, 'todo_list/room.html', {})

def home(request) :
    # return render(request, 'todo_list/home.html', {})
    if request.method == 'POST' :
        form = ListForm(request.POST or None)

        if form.is_valid() :
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item Has Been Added To List!'))
            return render(request, 'todo_list/home.html', {'all_items' : all_items})

    else :
        all_items = List.objects.all
        return render(request, 'todo_list/home.html', {'all_items' : all_items})

def delete(request, list_id) :
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted'))
    return redirect('todo_list:home')

def cross_off(request, list_id) :
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo_list:home')

def uncross(request, list_id) :
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo_list:home')

def edit(request, list_id) :
    if request.method == 'POST' :
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid() :
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('todo_list:home')

    else :
        item = List.objects.get(pk=list_id)
        return render(request, 'todo_list/edit.html', {'item' : item})
