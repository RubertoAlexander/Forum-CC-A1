from flask import render_template, request, redirect

from app.models import fs_users, gcs_user_images
from app import app

@app.route('/register', methods=['GET'])
def register_page():

    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    unique_id = fs_users.check_unique_id(request.form['id'])
    unique_username = fs_users.check_unique_username(request.form['username'])

    if not unique_id:
        return render_template('register.html', registerError='The ID already exists')
    elif not unique_username:
        return render_template('register.html', registerError='The username already exists')
    else:
        fs_users.add_user(request.form['id'], request.form['username'], request.form['password'])
        gcs_user_images.upload_image(request.files['image'], request.form['id'])
        return redirect('/login')

