from flask import Flask, render_template, jsonify # import the Flask class and render_template function from the flask module
from flask_mqtt import Mqtt
import json

app = Flask(__name__) # create an app instance of Flask

app.config['MQTT_BROKER_URL'] = 'broker.mqttdashboard.com'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'user'
app.config['MQTT_PASSWORD'] = 'secret'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds

mqtt = Mqtt(app)

sound = 20
light = 30
motion = 0
temperature = 0
humidity = 0

@app.route("/dashboard") # at the endpoint /dashboard
def get_dashboard(): # call the get_dashboard method
    print("get_dashboard method called!")
    return render_template('dashboard.html')

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('GFNCI/PUBLISH')
    print("Connected!")

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):

    global sound
    global light
    global motion
    global temperature
    global humidity

    str_message = str(message.payload.decode('utf-8'))
    print('Message received=%s' % str_message)
    message = json.loads(str_message)
    print('Message=%s' % message)

    sound = message.get('sound')
    light = message.get('light')
    humidity = message.get('humidity')
    motion = message.get('motion')
    temperature = message.get('temperature')

    print('Sound=%s' % sound)

    print('Light=%s' % light)

    print('Humidity=%s' % humidity)

    print('Motion=%s' % motion)

    print('Temperature=%s' % temperature)

@app.route('/_stuff', methods = ['GET'])
def stuff():

    global sound
    global light
    global motion
    global temperature
    global humidity

    return jsonify(sound = sound, light = light, motion = motion, temperature = temperature, humidity = humidity)

if __name__ == "__main__": # on running python app.py
    app.run(debug=True) # run the flask app in debug mode
    # app.run() # run the flask app without debug mode
