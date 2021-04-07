from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket(u'forum-cc-a1-task1-s3663431.appspot.com')

def upload_image(image_file, user_id) -> None:
    blob = bucket.blob('user_images/'+ user_id + '.jpg')
    blob.upload_from_file(image_file)