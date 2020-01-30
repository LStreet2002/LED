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
            # LED on
        else:
            print("LED off")
            # LED off
        return "End"
    
    if request.method=="GET":
        return str(led)




if __name__ == '__main__':
    app.run(debug=True)

