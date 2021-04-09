from google.cloud import storage
from random import randrange

client = storage.Client()
bucket = client.get_bucket(u'forum-cc-a1-task1-s3663431.appspot.com')

def upload_image(image_file, user_id) -> None:
    blob = bucket.blob('user_images/'+ user_id + '.jpg')
    blob.upload_from_file(image_file)
    blob.make_public()

def get_image_url(filename):
    blob = bucket.get_blob(u'user_images/' + filename)
    if blob == None:
        return None
    else:
        return blob.public_url

def get_user_image(user_id):
    user_image = get_image_url(user_id + '.jpg')
    if user_image == None:
        default_url = get_default_image_url(user_id)
        user_image = get_image_url(default_url)

    return user_image

def get_default_image_url(user_id):
    last_char = user_id[-1]
    if last_char.isdigit():
        filename = last_char + '.jpg'
    else:
        filename = str(randrange(10)) + '.jpg'

    return filename