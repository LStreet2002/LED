
from sense_hat import sense_hat
from flask import Flask, render_template, request, json

app = Flask(__name__)
led=False

@app.route('/')
def start():
    return render_template('base.html')

@app.route('/status', methods=['POST','GET'])
def status():
    global led
    if request.method=="POST":
        content = request.get_json()
        led=content['led']
        if(led):
            print("LED on")
            sense= SenseHat()

            r= 255
            g= 255
            b= 255

             sense.clear((r, g, b))
        else:
            print("LED off")
             sense.clear(())
           

     
            # LED off
        return "End"

    if request.method=="GET":
        return str(led)
