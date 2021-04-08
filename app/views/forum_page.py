import time
from app.models import fs_messages, fs_users, gcs_message_images, gcs_user_images
from flask import render_template, request, redirect

from app import app

@app.route('/', methods=['GET'])
def forum_page():
    username = request.cookies.get('username')
    user_id = request.cookies.get('id')

    if user_id:
        user_image_url = gcs_user_images.get_user_image(user_id)
        posts = fs_messages.get_latest_messages(10)

        post_list = []
        for post in posts:
            post_user = post.get('user').get()

            post_list.append( {
                'post_details' : post,
                'username' : post_user.get('user_name'),
                'user_image' : gcs_user_images.get_user_image(post_user.get('id')),
                'post_image' : gcs_message_images.get_image_url(post.id),
                'post_datetime' : post.get('post_datetime').strftime('%d/%m/%Y %I:%M %p')
            })
        
        return render_template('forum.html', 
            user_name=username,
            user_image=user_image_url,
            posts=post_list
            )
    else:
        return redirect('/login')

@app.route('/', methods=['POST'])
def post_message():
    user = fs_users.get_user_by_id(request.cookies.get('id'))
    subject = request.form['subject']
    message = request.form['message-text']
    image = request.files['message-image']

    message_uploaded = fs_messages.add_message(user.id, subject, message)
    print(message_uploaded)

    image_pass = False
    if image.filename != '':
        gcs_message_images.upload_image(image, message_uploaded)

    return redirect('/')