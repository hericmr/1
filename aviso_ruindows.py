from twilio.rest import Client

account_sid = "AC377b6ee9bc32f9a31a0030669e0bc991"
auth_token  = "0c8b877f19774742992778a62c37f162"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5513991812210",
    from_="+19284558259",
    body="-------------------------------------------- Héric, alguém acaba de ligar seu PC utilizando Ruindows")

print(message.sid)