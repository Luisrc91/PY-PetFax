from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "My First App of Doom!"


# pets index route
@app.route('/pets')
def pets(): 
    return 'These are our pets available for adoption!'
