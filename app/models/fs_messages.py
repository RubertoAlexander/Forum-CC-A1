from datetime import datetime
import firebase_admin
from app.models.fs_users import COLLECTION
from . import db, firestore

COLLECTION = u'messages'

def add_message(user_key, subject, message):
    message = {
        u'user' : db.collection(u'users').document(user_key),
        u'subject' : subject,
        u'message' : message,
        u'post_datetime' : datetime.now()
    }

    doc_ref = db.collection(COLLECTION).add(message)
    return doc_ref[1].id

def get_latest_messages(num_messages):
    query = db.collection(COLLECTION).order_by(u'post_datetime', direction=firestore.Query.DESCENDING).limit(num_messages).get()
    message_list = list(query)
    return message_list