import os
from flask import Flask, jsonify, request, render_template
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def index():

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    apn_sid = os.environ['TWILIO_APN_CREDENTIAL_SID']
    gcm_sid = os.environ['TWILIO_GCM_CREDENTIAL_SID']
    service_sid = os.environ['TWILIO_NOTIFICATION_SERVICE_SID']

    return render_template('index.html',
                           account_sid = account_sid,
                           auth_token = auth_token,
                           apn_sid = apn_sid,
                           gcm_sid = gcm_sid,
                           service_sid = service_sid)

@app.route('/register', methods=['POST'])
def register():
    # get credentials for environment variables
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    service_sid = os.environ['TWILIO_NOTIFICATION_SERVICE_SID']

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # Body content
    content = request.get_json()
    print(content)

    # Get a reference to the notification service
    service = client.notify.services(service_sid)

    # Create the binding
    binding = service.bindings.create(
        endpoint=content["endpoint"],
        identity=content["identity"],
        binding_type=content["bindingType"],
        address=content["address"])

    print(binding)

    # Return success message
    return jsonify(message="Binding created!")

if __name__ == '__main__':
    app.run(debug=True)
