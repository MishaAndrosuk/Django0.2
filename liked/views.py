from django.shortcuts import redirect, render
from django.contrib import messages

from liked.liked import add_to_liked, clear_liked, get_liked
from films.models import Film

def index(request):
    items = get_liked(request.session)
    films = Film.objects.filter(id__in=items.keys())

    return render(request, "liked/index.html", {"films": films})

def add(request, id, quantity = 1):
    if Film.objects.get(id=id) is None:
        messages.error(request, "Product not found!")
        return redirect("/liked")

    add_to_liked(request.session, id, quantity)
    messages.success(request, "Film added to liked!")

    return redirect("/liked")

def clear(request):
    clear_liked(request.session)
    messages.success(request, "Liked cleared!")

    return redirect("/liked")

