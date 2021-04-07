import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'forum-cc-a1-task1-s3663431',
})

db = firestore.client()

def fetch_user_by_id(id) -> list:
    query = db.collection(u'users').where(u'id', u'==', id).limit(1).get()
    user_list = list(query)
    return user_list

def fetch_user_password(doc_id) -> str:
    user = db.collection(u'users').document(doc_id).get()
    print(user.to_dict())
    return user.get('password')