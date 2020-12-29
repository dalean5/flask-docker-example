import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect, secure_filename
from config import get_env_variable

basedir = os.path.abspath(os.path.dirname(__file__))

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config.from_object(get_env_variable('APP_SETTINGS'))

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/<echo>/')
def echo_name(echo):
    return render_template("echo.html", echo=echo)


@app.route('/file-upload/', methods=['GET', 'HEAD', 'OPTIONS', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template("file-upload.html")
    elif request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(basedir, 'uploads', filename))
        return redirect(url_for('upload_file'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)