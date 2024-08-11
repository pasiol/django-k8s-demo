import django
from django.db import IntegrityError, DatabaseError, transaction
from django.shortcuts import render
from django.conf import settings
from cinfo.models import Worker, Request
import time

def index(request):
    w = None
    succeed = False
    while not succeed:
        try:
            w = Worker.objects.get(worker_id=settings.WORKER_ID)
            succeed = True
        except DatabaseError:
            time.sleep(10)
        except Worker.DoesNotExist:
            new_worker = Worker()
            new_worker.worker_id = settings.WORKER_ID
            new_worker.hostname = settings.HOSTNAME
            new_worker.fqdn = settings.FQDN
            new_worker.ip_address = settings.IP_ADDRESS
            new_worker.mac_address = settings.MAC_ADDRESS
            new_worker.save()
            w = new_worker
            succeed = True
    succeed = None
    save_new_request(request)
    worker_requests = Request.objects.filter(worker_id=settings.WORKER_ID).order_by("-timestamp")[:40]

    context = {
        "worker_id": w.worker_id,
        "ip_address": w.ip_address,
        "mac_address": w.mac_address,
        "hostname": w.hostname,
        "requests": worker_requests,
    }
    w = None
    worker_requests = None
    return render(request, "index.html", context=context)

def version(request):
    context = {
        "version": django.get_version()
    }
    return render(request, "version.html", context=context)

def count(request):
    w = None
    succeed = False
    while not succeed:
        try:
            w = Worker.objects.get(worker_id=settings.WORKER_ID)
            succeed = True
        except DatabaseError:
            time.sleep(10)
        except Worker.DoesNotExist:
            new_worker = Worker()
            new_worker.worker_id = settings.WORKER_ID
            new_worker.hostname = settings.HOSTNAME
            new_worker.fqdn = settings.FQDN
            new_worker.ip_address = settings.IP_ADDRESS
            new_worker.mac_address = settings.MAC_ADDRESS
            save_object(new_worker)
            w = new_worker
            succeed = True

    save_new_request(request)

    succeed = False
    context = {}
    while not succeed:
        try:
            count_of_worker_requests = Request.objects.filter(worker_id=settings.WORKER_ID).count()
            all_workers_with_same_mac_address = \
                Worker.objects.filter(mac_address=settings.MAC_ADDRESS).values("worker_id")
            count_of_pod_requests = \
                Request.objects.filter(worker_id__in=all_workers_with_same_mac_address).count()
            count_of_all_requests = Request.objects.filter().count()
            context = {
                "worker_id": w.worker_id,
                "ip_address": w.ip_address,
                "mac_address": w.mac_address,
                "hostname": w.hostname,
                "count_of_all_requests": count_of_all_requests,
                "count_of_worker_requests": count_of_worker_requests,
                "percentage_worker": round((count_of_worker_requests / count_of_all_requests) * 100, 1),
                "count_of_pod_requests": count_of_pod_requests,
                "percentage_pod": round((count_of_pod_requests / count_of_all_requests) * 100, 1),

            }
            succeed = True
        except DatabaseError:
            time.sleep(10)

    return render(request, "count.html", context=context)


def get_requests(r):
    w = Worker.objects.get(worker_id=settings.WORKER_ID)
    new_request = Request()
    new_request.user_agent = r.headers["User-Agent"]
    new_request.worker_id = settings.WORKER_ID
    new_request.save()
    worker_requests = Request.objects.filter(worker_id=settings.WORKER_ID).order_by("-timestamp")[:40]

    context = {
        "worker_id": w.worker_id,
        "ip_address": w.ip_address,
        "mac_address": w.mac_address,
        "hostname": w.hostname,
        "requests": worker_requests,
    }
    w = None
    return context


def save_new_request(r):
    w = Worker.objects.get(worker_id=settings.WORKER_ID)
    new_request = Request()
    new_request.user_agent = r.headers["User-Agent"]
    new_request.worker_id = settings.WORKER_ID
    save_object(new_request)
    w = None
    new_request = None


@transaction.atomic
def save_object(o):
    succeed = False
    while not succeed:
        try:
            with transaction.atomic():
                o.save()
                succeed = True
        except IntegrityError:
            time.sleep(10)
    succeed = None
    o = None

