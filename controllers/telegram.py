import requests
import controllers.firestore as firestore

class TelegramController:
    def __init__(self, user):
        self.user = user
        self.url = "https://api.telegram.org/bot5845155383:AAFj-63Q2SvbI_LW6QeeUpjAhVIhlsji8xs/"

    def send_message(self, message):
        requests.get(self.url + "sendMessage?chat_id=" + str(self.user.id) + "&text=" + message)

    def send_photo(self, photo_url):
        json = {
            "chat_id": self.user.id,
            "photo": photo_url
        }
        requests.post(self.url + "sendPhoto", json=json)

    def greet(self):
        self.send_message("MEOW " + self.user.first_name + " 😺!")