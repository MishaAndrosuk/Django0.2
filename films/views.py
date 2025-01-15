from django.shortcuts import render, redirect
from django.http import HttpResponse

from films.forms.create import CreateFilm
from films.forms.edit import EditFilm
from films.models import Film
from django.core.paginator import Paginator


def list(request):
    films = Film.objects.all()
    paginator = Paginator(films, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "list_films.html", {"page_obj": page_obj})

def detail(request, id):
    try:
        film = Film.objects.get(id=id)
        return render(request, "film_details.html", {"film": film})
    except Film.DoesNotExist:
        return HttpResponse("User not found", status=404)
    
def delete(request, id):
    try:
        film = Film.objects.get(id=id)

        if film.photo and film.photo.path:
            film.photo.delete(save=False)

        film.delete()
        return redirect("/films/")
    except Film.DoesNotExist:
        return HttpResponse("Film not found", status=404)


def create(request):
    form = CreateFilm()

    if request.method == "POST":
        form = CreateFilm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/films/")
        else:
            return render(request, "create_film.html", {"form": form})

    return render(request, "create_film.html", {"form": form})


def edit(request, id):
    film = Film.objects.get(id=id)

    if film is None:
        return HttpResponse("Film not found", status=404)
    
    form = EditFilm(instance=film)

    if request.method == "POST":
        form = EditFilm(request.POST, request.FILES, instance=film)

        if request.FILES and film.photo:
            film.photo.delete()

        if form.is_valid():
            if request.FILES.get('photo'):
                if film.photo:
                    film.photo.delete()  
        form.save()  
        return redirect("/films/")
       
    return render(request, "edit_film.html", {"form": form, "film": film})
    

def save_film(request, id):
    try:
        film = Film.objects.get(id=id)

        film.is_saved = not film.is_saved
        film.save()

        return redirect("/films/")
    except Film.DoesNotExist:
        return HttpResponse("Film not found", status=404)

def saved(request):
    saved_films = Film.objects.filter(is_saved=True)
    return render(request, "saved_films.html", {"films": saved_films})


def index(request):
    saved_films_count = Film.objects.filter(is_saved=True).count()
    return render(request, '_layout_films.html', {'saved_films_count': saved_films_count})


