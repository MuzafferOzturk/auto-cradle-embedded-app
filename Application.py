from subprocess import call
from flask import Flask, request
from Enums import EngineStatusEnum
from DCEngine import DCEngine

engine = DCEngine()
app = Flask(__name__)


@app.route('/')
def index():
    return 'Cradle App'


@app.route('/start', methods=['POST'])
def start():
    if status() == EngineStatusEnum.START.name:
        engine.start()
        return 'OK', 200
    else:
        return 'Already started', 500


@app.route('/stop', methods=['POST'])
def stop():
    engine.stop()
    return 'OK', 200


@app.route('/status')
def status():
    return engine.getstatus()


@app.route('/setSpeed', methods=['POST'])
def set_speed():
    if status() == EngineStatusEnum.START.name:
        speed = int(request.args.get('speed'))
        if speed >= 70:
            engine.setSpeed(speed)
            return 'OK', 200
        else:
            return 'Speed Low', 500
    else:
        return 'Before Start', 500


@app.route("/shutdown", methods=['POST'])
def shutdown():
    call("sudo shutdown -h now", shell=True)


if __name__ == '__main__':
    app.run(port=9000, host='192.168.1.6')
