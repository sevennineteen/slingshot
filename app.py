from flask import Flask, request, make_response, jsonify, Markup
from pyslinger import pyslinger
import simplejson as json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def load_item():
    if request.method == 'GET':
        return Markup('''
            <h1>Slingshot</h1>
            Send a JSON payload to this URL like so:<br> 
            <code>curl -F payload=@page_example.json %s</code>
            ''' % request.url)
    if request.method == 'POST' and 'payload' in request.files:
        payload = json.load(request.files['payload'])
        result = pyslinger.load_item(payload)
        return make_response(jsonify(result))

if __name__ == "__main__":
    app.run(debug=True)