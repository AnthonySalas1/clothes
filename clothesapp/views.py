from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse
from .models import Item
from .forms import itemForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def init(request):
    item_list = Item.objects.all()
    context = { 'item_list':item_list}
    return render(request, 'index.html', context)

def create(request):
    form = itemForm(request.POST, request.FILES)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create.html', {'form':form})

def update(request, pk):
    obj = get_object_or_404(Item, pk=pk)
    form  = itemForm(request.POST or None, instance= obj)

    if form.is_valid():
        form.save()
        return init(request)
    context = {'form':form}
    return render(request, "update.html", context)

def delete(request, pk):
    obj = get_object_or_404(Item, pk=pk)
    obj.delete()
    return redirect('/') 



    


