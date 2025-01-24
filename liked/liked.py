LIKED_KEY = "film_liked_key"

def add_to_liked(session, id, quantity=1):
    liked = session.get(LIKED_KEY, {})
    
    id = str(id)
    
    if id not in liked:
        liked[id] = quantity
    else:
        liked[id] += quantity
    
    session[LIKED_KEY] = liked

def get_liked(session):
    return session.get(LIKED_KEY, {})

def clear_liked(session):
    session[LIKED_KEY] = {}

def get_count(session):
    return len(get_liked(session))

def delete_from_liked(session, id):
    liked = get_liked(session)

    id = str(id)

    if id in liked:
        del liked[id]
        session[LIKED_KEY] = liked
        return True
    return False


