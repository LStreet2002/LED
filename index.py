import RPi.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    return render_template('index.html')


@app.route('/on')
def turnOn():
    GPIO.output(18, GPIO.HIGH)
    return render_template('index.html')


@app.route('/off')
def turnOff():
    GPIO.output(18, GPIO.LOW)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
