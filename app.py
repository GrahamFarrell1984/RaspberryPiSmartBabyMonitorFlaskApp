from flask import Flask, render_template # import the Flask class and render_template function from the flask module
from flask_mqtt import Mqtt

app = Flask(__name__) # create an app instance of Flask

app.config['MQTT_BROKER_URL'] = 'broker.mqttdashboard.com'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'user'
app.config['MQTT_PASSWORD'] = 'secret'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds

mqtt = Mqtt(app)

# data=[
#     {
#         'name':'Audrin',
#         'place': 'kaka',
#         'mob': '7736'
#     },
#     {
#         'name': 'Stuvard',
#         'place': 'Goa',
#         'mob' : '546464'
#     }
# ]

@app.route("/dashboard") # at the endpoint /dashboard
def get_dashboard(): # call the get_dashboard method
    # mqtt.subscribe('GFNCI/PUBLISH')
    # mqtt.publish('GFNCI/PUBLISH', 'hello world')
    return render_template('dashboard.html', payload = payload) # return the dashboard.html template

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('GFNCI/PUBLISH')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(topic=message.topic, payload=message.payload.decode())

if __name__ == "__main__": # on running python app.py
    # app.run(debug=True) # run the flask app in debug mode
    app.run() # run the flask app without debug mode
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)ate('dashboard.html')
