from flask import Flask, request, jsonify, Markup
from pyslinger import pyslinger
import simplejson as json
from markdown import markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def load_item():
    if request.method == 'GET':
        # show usage docs
        return Markup(markdown(open('README.md').read()))
    if request.method == 'POST' and 'payload' in request.files:

        # Update any pyslinger constants passed
        # cq_server, username, password, static_root
        for field in request.form:
            setattr(pyslinger, field.upper(), request.form[field])

        payload = json.load(request.files['payload'])
        result = pyslinger.load_item(payload)
        return jsonify(result)

if __name__ == "__main__":
    app.run()
