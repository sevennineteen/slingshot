from flask import Flask, request, jsonify, Markup
from pyslinger import pyslinger
import simplejson as json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def load_item():
    if request.method == 'GET':
        return Markup('''
            <h1>Slingshot</h1>
            <pre>
            Send a JSON payload to this URL like so:

            curl -F payload=@page_example.json %s</code>

            Use -F to set additional configurations:

            * cq_server       [ http://localhost:4502 ]
            * username        [ admin ]
            * password        [ admin ]
            * static_root     [ . ]

            For example:

            curl -F payload=@asset_example.json -F username=me -F password=P@55w0rd -F static_root=/my/assets http://localhost:5000/
            </pre>

            ''' % request.url)
    if request.method == 'POST' and 'payload' in request.files:

        # Update any pyslinger constants passed
        # cq_server, username, password, static_root
        for field in request.form:
            setattr(pyslinger, field.upper(), request.form[field])

        payload = json.load(request.files['payload'])
        result = pyslinger.load_item(payload)
        return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)