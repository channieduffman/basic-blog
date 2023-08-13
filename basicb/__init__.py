import os

from flask import Flask


def create_app(test_config=None):
    # establish instance of Flask
    app = Flask(__name__, instance_relative_config=True)
    # set default config values
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'basicb.sqlite'),
    )

    # check for test configuration
    if test_config is None:
        # load config.py is not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # else load test config
        app.config.from_mapping(test_config)

    # ensure existence of instance folder
    try:
        os.makedirs(app.instance_path)
    except OSError: # thrown if already exists
        pass

    # default test route
    @app.route('/hello')
    def hello():
        return 'Hello, world!'
    
    from . import db
    db.init_app(app)
    
    return app