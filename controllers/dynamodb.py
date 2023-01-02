import boto3
from user import User

class DynamoDB:
    def __init__(self, table_name):
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(self.table_name)

    def add_user(self, user: User):
        # check if user exists
        response = self.table.get_item( Key = { 'id': user.id } )
        if 'Item' in response:
            print('user already exists')
        else:
            self.table.put_item( Item = { 'id': user.id, 'first_name': user.first_name } )
            print('added user')

    def get_user_by_id(self, telegram_id):
        response = self.table.get_item( Key = { 'id': telegram_id } )
        if 'Item' in response:
            print(response['Item']['id'], response['Item']['first_name'])
        else:
            print('user does not exist')

    def delete_user(self, telegram_id):
        # check if user exists
        response = self.table.get_item( Key = { 'id': telegram_id } )
        if 'Item' in response:
            self.table.delete_item( Key = { 'id': telegram_id } )
            print('deleted user')
        else:
            print('user does not exist')

    def get_all_users(self):
        response = self.table.scan()
        print(response['Items'])
        print(response)
        return response['Items']

    def delete_all_users(self):
        response = self.table.scan()
        for user in response['Items']:
            self.table.delete_item( Key = { 'id': user} )
        print('deleted all users')