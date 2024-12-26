from django.shortcuts import render, redirect 
from django.http import HttpResponse

from films.forms.create import CreateFilm
from films.forms.edit import EditFiml
from films.models import Film



def list(request):
    films = Film.objects.all()
    return render(request, "film_list.html", {"films": films})

def detail(request, id):
    try:
        film = Film.objects.get(id=id)
        return render(request, "film_details.html", {"film": film})
    except Film.DoesNotExist:
        return HttpResponse("User not found", status=404)
    
def delete(request, id):
    try:
        film = Film.objects.get(id=id)
        film.delete()
        return redirect("/films/")
    except Film.DoesNotExist:
        return HttpResponse("Film not found", status=404)


def create(request):

    form = CreateFilm()

    if request.method == "POST":
        form = CreateFilm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/films/")

    return render(request, "create_film.html", {"form": form})

def edit(request, id):
    try:
        film = Film.objects.get(id=id)
        form = EditFiml(instance=film)

        if request.method == "POST":
            form = CreateFilm(request.POST, instance=film)

            if form.is_valid():
                form.save()
                return redirect("/films/")

        return render(request, "edit_film.html", {"form": form})
    except Film.DoesNotExist:
        return HttpResponse("Film not found", status=404)