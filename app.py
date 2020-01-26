from flask import Flask, request
from pymessenger.bot import Bot
import os

app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)

commands_list = ["!trip", "!budget", "!location", "!trains", "!help"]
DESTINATION = "Groningen, Netherlands"


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        # Before allowing people to message your bot, Facebook has implemented a verify token
        # that confirms all requests that your bot receives came from Facebook.
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text') in commands_list:
                        command = message['message'].get('text')
                        response_sent_text = get_message(command)
                        send_message(recipient_id, response_sent_text)

    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"


def get_message(command):
    response = None

    if command == '!trip':
        response = DESTINATION
    elif command == '!help':
        response = "Comenzi TravelBot:\n" \
                   "!trip, !budget,!location,!trains"
    elif command == '!budget':
        response = "Buget Olanda Aproximat(de persoana):\n" \
                   "Transport: 70 Euro\n" \
                   "    -Transport Groningen\n" \
                   "    -Transport Haga + Amsterdam\n" \
                   "    -Transport Aeroport\n" \
                   "Mancare:30 Euro"
    elif command == '!location':
        response = 'https://goo.gl/maps/Fv7bADuswqeYoEvv7'
    elif command == '!trains':
        response = "Puteti cumpara biletele de tren de aici:\n" \
                   "https://www.treinreiziger.nl/goedkope-enkele-reis-naar-schiphol-rotterdam-en-eindhoven/"

    return response


if __name__ == '__main__':
    app.run()
