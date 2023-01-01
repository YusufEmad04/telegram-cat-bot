import requests

from controllers.bucket import BucketController


class TelegramController:
    def __init__(self, user):
        self.user = user
        self.url = "https://api.telegram.org/bot5845155383:AAFj-63Q2SvbI_LW6QeeUpjAhVIhlsji8xs/"
        self.handle_message(user.text)

    def send_message(self, message):
        requests.get(self.url + "sendMessage?chat_id=" + str(self.user.id) + "&text=" + message)

    def send_photo(self, photo_url):
        json = {
            "chat_id": self.user.id,
            "photo": photo_url
        }
        requests.post(self.url + "sendPhoto", json=json)

    def send_video(self, video_url):
        json = {
            "chat_id": self.user.id,
            "video": video_url
        }
        requests.post(self.url + "sendVideo", json=json)

    def send_media(self, media_url):
        if media_url[1].endswith(".mp4"):
            self.send_video(media_url[0])
        else:
            self.send_photo(media_url[0])

    def send_voice(self, audio_file):
        data = {
            "chat_id": self.user.id,
        }
        requests.post(self.url + "sendVoice", data=data, files={"voice": audio_file})

    def greet(self):
        self.send_message("MEOW " + self.user.first_name + " 😺!")

    def handle_message(self, message):
        if message == "/meow":
            # self.send_voice(BucketController().get_url_of_object("meows/meow2.ogg"))
            self.send_voice(BucketController().get_file_bytes("meows/meow2.ogg"))
        else:
            self.greet()
            self.send_media(BucketController().get_random_object_url())