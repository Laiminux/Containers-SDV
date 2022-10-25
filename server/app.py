from flask import Flask, render_template, request
from datetime import datetime
from db import init_db
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics


def create_app(test_config=None):
    app = Flask(__name__, static_folder='templates')

    app.config['SECRET_KEY'] = "DaKey"

    if test_config is None:
        app.config['DATABASE']='db'
    else :
        app.config.update(test_config)

    with app.app_context():
        init_db()

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html'),200

    return app

if __name__ == "__main__":
    app = create_app()
    register_metrics(app, app_version="v0.1.2", app_config="staging")
    dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})
    run_simple(hostname="0.0.0.0", port=80, application=dispatcher)