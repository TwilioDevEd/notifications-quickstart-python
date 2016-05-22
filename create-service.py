import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
apn_sid = os.environ['TWILIO_APN_CREDENTIAL_SID']
gcm_sid = os.environ['TWILIO_GCM_CREDENTIAL_SID']

# Authenticate with Twilio
client = Client(account_sid, auth_token)

# Create a user notification service instance
service_data = dict(friendly_name='My First Notifications App')
if apn_sid:
    print 'Adding APN Credentials to service'
    service_data['apn_credential_sid'] = apn_sid
else:
    print 'No APN Credentials configured - add in .env, if available.'

if gcm_sid:
    print 'Adding GCM Credentials to service'
    service_data['gcm_credential_sid'] = gcm_sid
else:
    print 'No GCM Credentials configured - add in .env, if available.'

service = client.notifications.v1.services.create(**service_data)
print service
