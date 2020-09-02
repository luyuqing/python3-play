import os
import datetime

import flask


app = flask.Flask(__name__)


COLOR = os.environ.get('COLOR', 'turquoise')
FILEPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'file.txt'))


@app.route('/')
def index():
    return flask.render_template('index.html', color=COLOR)


@app.route('/edit')
def edit():
    with open(FILEPATH, 'a') as f:
        f.write('new line {} \n'.format(datetime.datetime.now()))

    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True, threaded=True)
