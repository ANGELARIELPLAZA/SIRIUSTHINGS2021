import paho.mqtt.client as mqtt
from flask import Flask, render_template, request

app = Flask(__name__)

#mqtt = mqtt.Client()
#mqtt.connect("localhost", 1883, 60)
#mqtt.loop_start()
# Mesa 1                 
topic1 = "mesa1"   


@app.route("/", methods=["GET", "POST"])
def home():
      return render_template('raspi.html')


@app.route("/jetson", methods=["GET", "POST"])
def jetson():
	return render_template('jetson.html')


@app.route("/arduino", methods=["GET", "POST"])
def jetson():
	datos = request.form.to_dict(flat=True)
  print(datos)
   #########################################
  valores1 = datos.get("mesa1")
   #########################################
  print(valores1)
  return render_template('arduino.html')


@app.route("/esp8266", methods=["GET", "POST"])
def jetson():
	datos = request.form.to_dict(flat=True)
  print(datos)
   #########################################
  valores1 = datos.get("mesa1")
   #########################################
  print(valores1)

	return render_template('esp8266.html')



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8181, debug=True)
