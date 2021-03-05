from flask import *
from snscrape.modules.twitter import *
app = Flask(__name__)

func = {
    'hashtag': TwitterHashtagScraper,
    'user': TwitterUserScraper,
}

keys = 'url date content id username outlinks outlinksss tcooutlinks tcooutlinksss'.split()

@app.route('/', methods=['GET', 'POST'])
def index():
    table = []

    if request.method == "POST":
        data = request.form

        scrape = func[
            data['type']
        ]
        
        gen = scrape(
            data['query'] + ' lang:en'
        ).get_items()

        # Tweet objects
        tweets = [
            next(gen)
            for i in range(int(data['count']))
        ]

        # Tweet dicts
        table = [
            dict(zip(keys, list(t)))
            for t in tweets
        ]

    return render_template(
        'index.html',
        textarea=json.dumps(
            table,
            indent=4,
        )
    )

app.run(debug=True, port=8080)