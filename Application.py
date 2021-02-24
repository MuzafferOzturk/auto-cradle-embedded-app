from flask import Flask

from DCEngine import DCEngine

engine = DCEngine()
app = Flask(__name__)


@app.route('/')
def index():
    return 'Cradle App'


@app.route('/start')
def start():
    engine.start()
    return status()


@app.route('/stop')
def stop():
    engine.stop()
    return status()


@app.route('/status')
def status():
    return engine.getstatus()


if __name__ == '__main__':
    app.run(port=9000)
