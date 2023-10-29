from app.users import user, manager

def get_user():
    subject = user.User()
    # subject = manager.Manager()
    return subject
