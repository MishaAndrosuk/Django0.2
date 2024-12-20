from django.shortcuts import render, redirect 
from django.http import HttpResponse

from users.forms.create import CreateUser
from users.models import User

def list(request):
    users = User.objects.all()
    return render(request, "list.html", {"users": users})

def detail(request, id):
    try:
        user = User.objects.get(id=id)
        return render(request, "details.html", {"user": user})
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)
    
def delete(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return redirect("/users/list/")
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)


def create(request):

    form = CreateUser()

    if request.method == "POST":
        form = CreateUser(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/users/list/")

    return render(request, "create.html", {"form": form})