from flask import render_template, request, redirect

from app.models import fs_users
from app import app

@app.route('/login', methods=['GET'])
def login_page():

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    is_successful = authenticate()
    if is_successful:
        return redirect('/')
    else:
        return render_template('login.html', loginError='ID or password is invalid')

def authenticate():
    result = fs_users.get_user_by_id(request.form['id'])
    print(str(result))
    if result:
        password = fs_users.get_user_password(result[0].id)
        print(password)
        if password == request.form['password']:
            return True
        else:
            return False
    else:
        return False
