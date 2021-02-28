from flask import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html',
    )

app.run(debug=True, port=8080)