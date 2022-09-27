from twilio.rest import Client

account_sid = "AC377b6ee9bc32f9a31a0030669e0bc991"
auth_token = "0c8b877f19774742992778a62c37f162"
meu_numero = "+13991912210"
numero_twilio = "+19284558259"

cliente = Client(account_sid, token)

mensagem = """
<Response>
<Say language="pt-BR">
Ei, Héric, ta tudo bem?. Se você estiver recebendo essa ligação é porque o código aqui deu certo!
</Say>
</Response>
"""

ligacao = cliente.calls.create(
    to=+13991812210,
    from_=+19284558259,
    twiml=mensagem
)
