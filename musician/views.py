from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.

def add_musician(request):
    if request.method == 'POST':
        frm = forms.M_form(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('seedata')
    
    else:
        form = forms.M_form()
    return render(request, 'musician.html', {'form':form})



def editt_musician(request, id):
    musi = models.Musician.objects.get(pk=id)
    frm = forms.M_form(instance=musi)
    if request.method == 'POST':
        frm = forms.M_form(request.POST, instance=musi)
        if frm.is_valid():
            frm.save()
            return redirect('seedata')
        
    return render(request, 'musician.html', {'form':frm})

