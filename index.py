import RPi.GPIO as GPIO
from flask import Flask, render_template, request

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

@app.route('/')
def start():  
    return render_template('index.html')

@app.route('/toggle', methods=['POST'])
def toggle():
    if request.form.get('button'):
        print("On")
        GPIO.output(18, GPIO.HIGH)
    else:
        print("Off")
        GPIO.output(18, GPIO.LOW)
    return render_template('index.html')

# Code needed in the HTML
# -----------------------
#<form method="post" action="/toggle">
#	<input type="checkbox" name="button"/>
#	<input type="submit"/>
#</form>
