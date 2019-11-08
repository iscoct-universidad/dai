from flask import Flask, render_template, send_from_directory, Response, request, url_for, redirect, session, make_response
from pickleshare import PickleShareDB
from os import urandom

db = PickleShareDB('./pickleDatabase')
db.clear()

app = Flask(__name__)
app.secret_key = urandom(16)

@app.route('/')
@app.route('/health')
def health():
    return 'The server is healthy'

@app.route('/static/<path:subpath>', methods = ['GET'])
def send_static_content(subpath):
    return send_from_directory('static', subpath, mimetype='*')

@app.route('/app', methods = ['GET'])
def serve_app():
    logged = 'username' in session
    username = session['username'] if logged else ''

    return render_app(logged=logged, user_name=username)

@app.route('/<path:path>')
def send_error(path):
    return f'The server does not support path: {path}'

@app.route('/app/signup', methods = ['POST'])
def sign_up():
    username = request.form.get('user_name')
    password = request.form.get('password')
    url_app = url_for('serve_app')

    if not exists_user(username, password):
        name = request.form.get('name')
        password_key = get_password_key_to_database(username, password)
        db[username] = username
        db[password_key] = password
        db[name] = name

        add_login_session(username)
        app_rendered = render_app(logged=True, user_name=username)
    else:
        app_rendered = render_app(error='The user was already created.')

    resp = make_response(app_rendered)
    resp.location = '/app'
    
    return resp

@app.route('/app/signin', methods = ['POST'])
def sign_in():
    username = request.form.get('user_name')
    password = request.form.get('password')
    exists = exists_user(username, password)
    url_app = url_for('serve_app')
    

    print('Hello world')
    if exists:
        add_login_session(username)
        app_rendered = render_app(logged=True, user_name=username)
    else:
        app_rendered = render_app(error='Login error')

    return redirect(url_app)

def add_login_session(username):
    session['username'] = username

def remove_login_session():
    session.pop('username', None)

@app.route('/app/logout', methods = ['POST'])
def log_out():
    app_url = url_for('serve_app')

    remove_login_session()

    return redirect(app_url)

def get_password_key_to_database(username, password):
    return username + password

def exists_user(username, password):
    key_password = get_password_key_to_database(username, password)

    username = db.get(username)
    password = db.get(key_password)

    return username and password

def render_app(error = False, logged = False, name='', user_name='', password=''):
    menu = ['Menu item 1', 'Menu item 2', 'Menu item 3']

    return render_template('app.html', menu = menu,
        error = error, logged = logged,
        user_name = user_name, password = password,
        name = name)