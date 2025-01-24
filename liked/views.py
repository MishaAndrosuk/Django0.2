from django.shortcuts import render

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from liked.liked import add_to_liked, clear_liked, get_liked, delete_from_liked
from films.models import Film

def index(request):
    items = get_liked(request.session)
    films = Film.objects.filter(id__in=items)
    
    return render(request, "liked/index.html", {"films": films})

def add (request, id, quantity=1):
    film = get_object_or_404(Film, id=id)
    add_to_liked(request.session, id, quantity)
    messages.success(request, f"Фільм '{film.title}' успішно додано до обраного!")

    return redirect("/liked")

def clear(request):
    clear_liked(request.session)  
    messages.success(request, "Liked cleared!")

    return redirect("/liked")

def delete_liked(request, id):
    if delete_from_liked(request.session, id):
        messages.success(request, "Film deleted from liked!")
    else:
        messages.error(request, "Film not found in liked!")
    return redirect("/liked")
