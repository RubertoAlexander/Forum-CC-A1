from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket(u'forum-cc-a1-task1-s3663431.appspot.com')

def upload_image(image_file, message_id) -> None:
    blob = bucket.blob('message_images/'+ message_id + '.jpg')
    blob.upload_from_file(image_file)
    blob.make_public()

def get_image_url(post_id):
    blob = bucket.get_blob(u'message_images/' + post_id + '.jpg')
    if blob == None:
        return None
    else:
        return blob.public_url
