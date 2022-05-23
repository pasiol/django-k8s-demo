import uuid
import socket
from django.apps import AppConfig
from django.conf import settings
from getmac import get_mac_address as gma


class CinfoConfig(AppConfig):
    name = "cinfo"
    verbose_name = "Django Kubernetes deployment demo"

    def ready(self):
        settings.WORKER_ID = uuid.uuid4()
        settings.HOSTNAME = socket.gethostname()
        settings.FQDN = socket.getfqdn()
        settings.IP_ADDRESS = socket.gethostbyname(settings.HOSTNAME)
        settings.MAC_ADDRESS = gma()

        #w = Worker()
        #w.worker_id = settings.WORKER_ID
        #w.hostname = settings.HOSTNAME
        #w.fqdn = settings.FQDN
        #w.mac_address = settings.MAC_ADDRESS
        #w.ip_address = settings.IP_ADDRESS
        #w.save()
