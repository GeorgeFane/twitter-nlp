from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

app.run(debug=True, port=8080)