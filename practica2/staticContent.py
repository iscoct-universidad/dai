from flask import Flask, render_template, send_from_directory, send_file, request
import os
from datetime import datetime, timedelta
from pathlib import Path

from randomImage import create_image
from printMandelbrot import pintaMandelbrot

app = Flask(__name__)

@app.route('/')
def health():
    return 'The server is healthy'

@app.route('/post/<post>')
def post(post):
    return render_template('post.html', name=post)

@app.route('/static/<path:subpath>')
def send_static_content(subpath):
    return send_from_directory('static', subpath, mimetype='*')

@app.route('/user/pepe')
def send_pepe():
    return 'This is the call for Pepe'

@app.route('/user/zerjillo')
def send_zerjillo():
    return 'This is the call for Zerjillo'

@app.route('/user/<user>')
def send_user(user):
    return f'This is the call for {user}'

@app.route('/<path:path>')
def send_error(path):
    return f'The server does not support the path {path}'

@app.route('/randomimage')
def random_image():
    create_image()

    return send_from_directory('static', 'newImage.svg', mimetype='image/svg+xml')

@app.route('/mandelbort')
def print_mandelbort():
    x1 = float(request.args.get('x1'))
    x2 = float(request.args.get('x2'))
    y1 = float(request.args.get('y1'))
    y2 = float(request.args.get('y2'))
    width = int(request.args.get('width'))
    iterations = int(request.args.get('iterations'))
    filename = f'static/mandelbort-x1_{x1}-y1_{y1}-x2_{x2}_y2-{y2}-width_{width}-iterations_{iterations}.png'
    path = Path(filename)

    if not path.exists():
        pintaMandelbrot(x1, y1, x2, y2, width, iterations, path)

    return send_file(filename)

@app.route('/removeoldfiles')
def remove_old_files():
    path = Path('static')

    for file in path.iterdir():
        stat = file.stat()
        fileModified = datetime.fromtimestamp(stat.st_mtime)

        if datetime.now() - fileModified > timedelta(hours=24) and file.suffix == '.png':
            os.remove(file)

    return 'Removed old files'

# These are examples in order to prove the above function

@app.route('/setmodificationtime/<path:path>')
def set_modification_time(path):
    file = Path(path)

    modificationTime = datetime.fromtimestamp(file.stat().st_mtime)
    modificationTime -= timedelta(days=1)
    stampModificationTime = modificationTime.timestamp()

    os.utime(file, (stampModificationTime, stampModificationTime))

    return 'Modified the modification time'


@app.route('/getmodificationtime/<path:path>')
def get_modification_time(path):
    file = Path(path)

    modificationTime = datetime.fromtimestamp(file.stat().st_mtime)

    return str(modificationTime.day)