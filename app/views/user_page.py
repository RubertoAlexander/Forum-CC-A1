from app.models import fs_messages, fs_users, gcs_message_images
from flask import render_template, request, redirect, flash
from app import app

# @app.route('//user/<id>/pwderror')
@app.route('/user/<id>', methods=['GET'])
def user_page(id):
    pwd_error = None
    if request.args.get('pwderror') == '1':
        pwd_error = 'The old password is incorrect'

    user = fs_users.get_user_by_id(id)
    print(fs_users.get_user_doc_ref(user.id))
    posts = fs_messages.get_all_messages_by_user(fs_users.get_user_doc_ref(user.id))

    post_list = []
    for post in posts:

        post_list.append( {
            'post_details' : post,
            'post_image' : gcs_message_images.get_image_url(post.id),
            'post_datetime' : post.get('post_datetime').strftime('%d/%m/%Y %I:%M %p')
        })

    return render_template('user.html',
        user_id=id,
        pwd_error=pwd_error,
        posts=post_list
    )

@app.route('/user/<id>/password', methods=['POST'])
def change_password(id):
    form_old_password = request.form['old-password']
    form_new_password = request.form['new-password']

    user = fs_users.get_user_by_id(id)
    user_password = fs_users.get_user_password(user.id)

    if user_password == form_old_password:
        fs_users.set_user_password(user.id, form_new_password)
        return redirect('/logout')
    else:
        return redirect('/user/'+id+'?pwderror=1')

@app.route('/user/<id>/update/<post>', methods=['POST'])
def update_post(id, post):
    print(request.form)
    subject = request.form[post+'-subject']
    message_text = request.form[post+'-message-text']
    if post+'-message-image' in request.files:
        image = request.files[post+'-message-image']
        if image.filename != '':
            gcs_message_images.upload_image(image, post)

    new_message = {
        'subject' : subject,
        'message' : message_text
    }
    fs_messages.update_message(post, new_message)

    return redirect('/')