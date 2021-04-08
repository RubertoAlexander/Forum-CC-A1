from datetime import datetime
from . import db, firestore

COLLECTION = 'messages'

def add_message(user_key, subject, message):
    message = {
        'user' : db.collection('users').document(user_key),
        'subject' : subject,
        'message' : message,
        'post_datetime' : datetime.utcnow()
    }
    result = db.collection(COLLECTION).add(message)
    return result[1].id

def get_message(message_key):
    message = db.collection(COLLECTION).document(message_key)
    return message

def update_message(message_key, message_dict):
    message = db.collection(COLLECTION).document(message_key)
    message.set(message_dict, merge=True)

def get_latest_messages(num_messages):
    query = db.collection(COLLECTION).order_by(u'post_datetime', direction=firestore.Query.DESCENDING).limit(num_messages)
    message_list = list(query.get())

    return message_list

def get_all_messages_by_user(user_ref):
    query = db.collection(COLLECTION).where(u'user', u'==', user_ref).order_by(u'post_datetime', direction=firestore.Query.DESCENDING)
    message_list = list(query.get())

    return message_list