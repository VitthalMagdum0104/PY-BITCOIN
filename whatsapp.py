from twilio.rest import Client
from config import account_sid, auth_token


def set_twilio_connection(account_sid, auth_token):
    """
    Sets twilio connection for whatsapp and sends message on Whatsapp.
    takes account_sid and account_token as parameter and returns client object.
    """
    client = Client(account_sid, auth_token)

    return client


def send_whatsapp(client, body):
    """
    takes message and twilio client connection as parameters and returns message ID  
    """
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=body,
        to='whatsapp:number with country code'
    )

    return message.sid


client = set_twilio_connection(account_sid, auth_token)
