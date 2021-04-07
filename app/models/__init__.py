import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'forum-cc-a1-task1-s3663431',
})

db = firestore.client()

from . import fs_users, gcs_user_images