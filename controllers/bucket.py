import boto3
import random

class BucketController:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.bucket = 'cats-for-telegram'

    def _get_tagging_of_object(self, key):
        response = self.s3.get_object_tagging(Bucket=self.bucket, Key=key)
        return response['TagSet']

    def get_objects_by_tag(self, tag_key, value):
        final_objects = []
        response = self.s3.list_objects_v2(Bucket=self.bucket)
        objects = response['Contents']
        for obj in objects:
            key = obj['Key']
            tags = self._get_tagging_of_object(key)
            for tag in tags:
                if tag['Key'] == tag_key and tag['Value'] == value:
                    final_objects.append(key)
        return final_objects

    def get_url_of_object(self, key):
        response = self.s3.generate_presigned_url('get_object', Params={'Bucket': self.bucket, 'Key': key})
        return response

    def set_tag_of_object(self, key, tag_key, value):
        self.s3.put_object_tagging(Bucket=self.bucket, Key=key, Tagging={'TagSet': [{'Key': tag_key, 'Value': value}]})

    def get_random_object_url(self):
        response = self.s3.list_objects_v2(Bucket=self.bucket)
        objects = response['Contents']
        random_object = random.choice(objects)
        key = random_object['Key']
        url = self.get_url_of_object(key)
        return url


