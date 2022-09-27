import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC377b6ee9bc32f9a31a0030669e0bc991']
auth_token = os.environ['0c8b877f19774742992778a62c37f162']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
         from_='whatsapp:+19284558259',
         to='whatsapp:+5513991812210'
     )

print(message.sid)

