# from flask import Flask, request
import json

from controllers.dynamodb import DynamoDB
from controllers.telegram import TelegramController
from controllers.bucket import BucketController
from user import User

# app = Flask(__name__)


def get_details_from_event_lambda(event):
    id = json.loads(event['body'])["message"]["from"]["id"]
    first_name = json.loads(event['body'])["message"]["from"]["first_name"]

    return id, first_name

def get_details_from_event_api(event):
    id = event["message"]["from"]["id"]
    first_name = event["message"]["from"]["first_name"]

    return id, first_name


# @app.route('/webhook', methods=['POST'])
# def webhook():
#     if request.method == 'POST':
#         id, first_name = get_details_from_event_api(request.json)
#
#         user = User(str(id), str(first_name))
#
#         controller = TelegramController(user)
#         controller.greet()
#
#         controller.send_photo(BucketController().get_random_object_url())
#
#         FirestoreController(cred_file="cred.json").add_user(user)
#
#     return 'OK'

def lambda_handler(event, context):
    id, first_name = get_details_from_event_lambda(event)

    user = User(id, str(first_name))

    controller = TelegramController(user)
    controller.greet()

    controller.send_media(BucketController().get_random_object_url())

    DynamoDB('users').add_user(user)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)
