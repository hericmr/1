from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
app = Flask(__name__)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("Oi, Héric, ta tudo bem?. Se você estiver recebendo essa ligação é porque o código aqui deu certo!")
    return str(resp)

if __name__ == "__main__":
    app.run()