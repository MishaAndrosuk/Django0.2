from django.shortcuts import render, redirect
from django.http import HttpResponse

from films.forms.create import CreateFilm
from films.forms.edit import EditFilm
from films.models import Film
from django.core.paginator import Paginator
from django.contrib import messages


def list(request):
    films = Film.objects.all()
    paginator = Paginator(films, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    liked_films = request.session.get('film_liked_key', [])
    liked_film_ids = set(map(int, liked_films))

    return render(request, 'list_films.html', {
        'page_obj': page_obj,
        'liked_film_ids': liked_film_ids
    })

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
        messages.success(request, "Фільм успішно видалено!")
        return redirect("/films/")
    except Film.DoesNotExist:
        return HttpResponse("Film not found", status=404)


def create(request):
    form = CreateFilm()

    if request.method == "POST":
        form = CreateFilm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Фільм успішно створено!")
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
        form = EditFilm(request.POST, instance=film, files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Фільм успішно відредаговано!")
            return redirect("/films/")

    return render(request, "edit_film.html", {"form": form, "film": film})
    

def index(request):
    films = Film.objects.all()
    return render(request, "list_films.html", {"films": films})

