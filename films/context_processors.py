from films.models import Film

def saved_films_count(request):
    count = Film.objects.filter(is_saved=True).count()
    return {'saved_films_count': count}