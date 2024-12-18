from django.shortcuts import render


from django.http import HttpResponse

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
    

