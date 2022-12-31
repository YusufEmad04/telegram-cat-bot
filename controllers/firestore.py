import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from user import User


class FirestoreController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FirestoreController, cls).__new__(cls)
            cred_file = "controllers/cred.json"
            cred = credentials.Certificate(cred_file)
            firebase_admin.initialize_app(cred)
            cls._instance.db = firestore.client()
        return cls._instance

    def get_all_users(self):
        users_ref = self.db.collection('users')
        docs = users_ref.stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')

    def delete_user(self, telegram_id):
        # check if user exists
        users_ref = self.db.collection('users')
        doc = users_ref.document(telegram_id).get()
        if doc.exists:
            users_ref.document(telegram_id).delete()
            print('deleted user')
        else:
            print('user does not exist')

    def get_user_by_id(self, telegram_id):
        users_ref = self.db.collection('users')
        doc = users_ref.document(telegram_id).get()
        if doc.exists:
            print(f'{doc.id} => {doc.to_dict()}')
        else:
            print('user does not exist')

    def add_user(self, user: User):
        # check if user exists
        users_ref = self.db.collection('users')
        doc = users_ref.document(user.id).get()
        if doc.exists:
            print('user already exists')
        else:
            users_ref.document(user.id).set({
                'first_name': user.first_name
            })
            print('added user')
