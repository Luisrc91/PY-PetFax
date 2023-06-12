from flask import Flask

def create_app():
    app = Flask(__name__)


    # homepage index route
    @app.route('/')
    def index():
        return "My First App of Doom! <br> Home page"

    # register pet.py
    from . import pet
    app.register_blueprint(pet.bp)


    from . import fact
    app.register_blueprint(fact.bp)

        
    return app
