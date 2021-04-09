from . import db

COLLECTION = u'users'

def get_user_by_id(id):
    query = db.collection(COLLECTION).where(u'id', u'==', id).limit(1).get()
    print(query)
    user_list = list(query)
    if len(user_list) > 0:
        return user_list[0]
    else:
        return None

def get_user_doc_ref(key):
    return db.collection(COLLECTION).document(key)

def get_user_by_username(username) -> list:
    query = db.collection(COLLECTION).where(u'user_name', u'==', username).limit(1).get()
    user_list = list(query)
    return user_list

def get_user_password(doc_id) -> str:
    user = db.collection(COLLECTION).document(doc_id).get()
    return user.get('password')

def set_user_password(doc_id, new_pw):
    user = db.collection(COLLECTION).document(doc_id)
    user.update({u'password' : new_pw})

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

def check_unique_id(id) -> bool:
    user_exists = get_user_by_id(id)
    unique_id = False if user_exists else True
    return unique_id

def check_unique_username(username) -> bool:
    user_exists = get_user_by_username(username)
    unique_username = False if user_exists else True
    return unique_username