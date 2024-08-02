from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        frm = forms.A_form(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('seedata')
    else:
        form = forms.A_form()
    return render(request, 'album.html', {'form':form})


def edit_album(request, id):
    albm = models.Album.objects.get(pk=id)
    frm = forms.A_form(instance=albm)
    if request.method == 'POST':
        frm = forms.A_form(request.POST, instance=albm)
        if frm.is_valid():
            frm.save()
            return redirect('seedata')
        
    return render(request, 'album.html', {'form':frm})


def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('seedata')





