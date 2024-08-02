from django.shortcuts import render
from album.models import Album
# from musician.models import Musician




def see_data(request):
    song = Album.objects.all()
    # singer = Musician.objects.all()
    return render(request, 'home.html', {'song':song})


