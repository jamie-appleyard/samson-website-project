from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.AWS_STATIC_LOCATION
    custom_domain = f'{bucket_name}.s3.amazonaws.com/{location}/'
    default_acl = 'public-read'

class PublicMediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    default_acl = 'public-read'
    file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False