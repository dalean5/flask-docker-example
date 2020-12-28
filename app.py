from flask import Flask
from config import get_env_variable

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
    return "<h1>Home page</h1><p>Welcome to my simple Flask app</p>"


@app.route('/<name>/')
def echo_name(name):
    return "<h1>Echo name</h1><p>Hi, {}!</p>".format(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)