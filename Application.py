from flask import Flask

from DCEngine import DCEngine

engine = DCEngine()
app = Flask(__name__)


@app.route('/')
def index():
    return 'Cradle App'


@app.route('/start', methods=['POST'])
def start():
    engine.start()
    return 'OK', 200


@app.route('/stop', methods=['POST'])
def stop():
    engine.stop()
    return 'OK', 200


@app.route('/status')
def status():
    return engine.getstatus()


if __name__ == '__main__':
    app.run(port=9000)
