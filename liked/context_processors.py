from liked.liked import get_count

def liked_count(request):
    return {'liked_count': get_count(request.session)}