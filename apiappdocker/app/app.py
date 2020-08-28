import os

import flask


app = flask.Flask(__name__)


COLOR = os.environ.get('COLOR', 'turquoise')


@app.route('/')
def index():
    return flask.render_template('index.html', color=COLOR)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True, threaded=True)
