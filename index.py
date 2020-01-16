import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    return render_template('index.html')


@app.route('/led', methods=['POST'])
def led():
    if request.form['button'] == 'On':
        print("on")
        GPIO.output(18, GPIO.HIGH)
        pass
    elif request.form['button'] == 'Off':
        print("off")
        GPIO.output(18, GPIO.LOW)
        pass
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
