import os
import sys
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
service_sid = os.environ['TWILIO_NOTIFICATION_SERVICE_SID']

# Authenticate with Twilio
client = Client(account_sid, auth_token)

# Create a reference to the user notification service
if service_sid:
  service = client.notifications.v1.services(service_sid)
  # Create a notification for a given identity
  identity = sys.argv[1]
  print 'Sending a notification to identity: ' + identity
  notification = service.notifications.create(
    identity=identity,
    body='Hello ' + identity + '!')
  print notification
else:
  print 'Please put a SID for a valid notification service in .env'
