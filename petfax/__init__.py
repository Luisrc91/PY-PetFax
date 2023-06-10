from flask import Flask

def create_app():

    app = Flask(__name__)

    # register pet.py
    from . import pet

    app.register_blueprint(pet.bp)

    # homepage index route
    @app.route('/')
    def index():
        return "My First App of Doom! <br> Home page"


    # pets index route
    # @app.route('/pets')
    # def pets(): 
    #     return 'These are our pets available for adoption!'
    
    return app
