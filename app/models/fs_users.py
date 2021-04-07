from . import db

COLLECTION = u'users'

def get_user_by_id(id) -> list:
    query = db.collection(COLLECTION).where(u'id', u'==', id).limit(1).get()
    user_list = list(query)
    return user_list

def get_user_by_username(username) -> list:
    query = db.collection(COLLECTION).where(u'user_name', u'==', username).limit(1).get()
    user_list = list(query)
    return user_list

def get_user_password(doc_id) -> str:
    user = db.collection(COLLECTION).document(doc_id).get()
    print(user.to_dict())
    return user.get('password')

def add_user(id, username, password) -> bool:
    user = {
        u'id' : id,
        u'user_name' : username,
        u'password' : password
    }

    doc_added = db.collection(COLLECTION).add(user)
    if doc_added:
        return True
    else:
        return False