import os
from twilio.rest import Client

account_sid = os.environ['AC377b6ee9bc32f9a31a0030669e0bc991']
auth_token = os.environ['0c8b877f19774742992778a62c37f162']
client = Client('AC377b6ee9bc32f9a31a0030669e0bc991','0c8b877f19774742992778a62c37f162')

call = client.calls.create(
                        twiml='<Response><Say>Olá Bruno, parabéns por ter se cadastrado como mesário nessa eleição!</Say></Response>',
                        to='+5513991812210',
                        from_='+19284558259'
                    )

print(call.sid)