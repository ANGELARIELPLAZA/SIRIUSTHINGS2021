from flask import Flask,render_template,url_for,request,redirect, make_response,send_file

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
       
    return render_template('raspi.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]

    Temperature = random() * 100
    Humidity = random() * 55

    data = [time() * 1000, Temperature, Humidity]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'
    return response


@app.route('/jetson')
def jetson():
    
    return render_template('jetson.html')

@app.route('/raspi')
def raspi():
    
    return render_template('raspi.html')
    
@app.route('/arduino')
def arduino():
    
    return render_template('arduino.html')
    


if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
