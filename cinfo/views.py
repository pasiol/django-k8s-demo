from django.shortcuts import render
from django.conf import settings
from cinfo.models import Worker, Request
import time


def index(request):
    try:
        w = Worker.objects.get(worker_id=settings.WORKER_ID)
    except Worker.DoesNotExist:
        new_worker = Worker()
        new_worker.worker_id = settings.WORKER_ID
        new_worker.hostname = settings.HOSTNAME
        new_worker.fqdn = settings.FQDN
        new_worker.ip_address = settings.IP_ADDRESS
        new_worker.mac_address = settings.MAC_ADDRESS
        new_worker.save()

    w = Worker.objects.get(worker_id=settings.WORKER_ID)
    new_request = Request()
    new_request.user_agent = request.headers["User-Agent"]
    new_request.worker_id = settings.WORKER_ID
    new_request.save()
    worker_requests = Request.objects.filter(worker_id=settings.WORKER_ID).order_by("-timestamp")[:40]

    count_of_worker_requests = Request.objects.filter(worker_id=settings.WORKER_ID).count()
    count_of_all_requests = Request.objects.filter().count()

    context = {
        "worker_id": w.worker_id,
        "ip_address": w.ip_address,
        "mac_address": w.mac_address,
        "hostname": w.hostname,
        "requests": worker_requests,
        "percentage_worker": round((count_of_worker_requests / count_of_all_requests) * 100, 1),
    }

    return render(request, "index.html", context=context)
