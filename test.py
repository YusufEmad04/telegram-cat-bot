from Controller import BucketController

bucket_controller = BucketController()
object = bucket_controller.get_random_object_url()
print(object)