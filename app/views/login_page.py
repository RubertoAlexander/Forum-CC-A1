from flask import render_template, request, redirect, make_response

from app.models import fs_users
from app import app

@app.route('/login', methods=['GET'])
def login_page():

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    is_successful = authenticate()
    if is_successful:
        user = fs_users.get_user_by_id(request.form['id'])
        username = user.get('user_name')
        response = make_response(redirect('/'))
        response.set_cookie('id', request.form['id'])
        response.set_cookie('username', username)
        return response
    else:
        return render_template('login.html', loginError='ID or password is invalid')

def authenticate():
    result = fs_users.get_user_by_id(request.form['id'])
    print(str(result))
    if result:
        password = fs_users.get_user_password(result.id)
        print(password)
        if password == request.form['password']:
            return True
        else:
            return False
    else:
        return False
