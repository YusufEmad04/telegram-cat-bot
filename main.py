from flask import Flask, request
import json
from Controller import BucketController, TelegramController

app = Flask(__name__)


def get_details_from_event_lambda(event):
    id = json.loads(event['body'])["message"]["from"]["id"]
    first_name = json.loads(event['body'])["message"]["from"]["first_name"]

    return id, first_name

def get_details_from_event_api(event):
    id = event["message"]["from"]["id"]
    first_name = event["message"]["from"]["first_name"]

    return id, first_name


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        id, first_name = get_details_from_event_api(request.json)
        controller = TelegramController(id, first_name)
        controller.greet()

        controller.send_photo(BucketController().get_random_object_url())
    return 'OK'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
