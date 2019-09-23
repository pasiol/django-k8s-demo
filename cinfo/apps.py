import uuid
from django.apps import AppConfig
from django.conf import settings


class CinfoConfig(AppConfig):
    name = "cinfo"
    verbose_name = "Django k8s demo, container info"

    def ready(self):
        settings.CONTAINER_ID = uuid.uuid4()
