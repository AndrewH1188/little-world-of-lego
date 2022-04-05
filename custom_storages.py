from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
