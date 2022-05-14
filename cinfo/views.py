import socket
from django.shortcuts import render
from django.conf import settings
from cinfo.models import Request


def get_server_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def index(request):

    new_request = Request()
    new_request.user_agent = request.headers["User-Agent"]
    new_request.container_id = settings.CONTAINER_ID
    new_request.save()
    this_container_requests = []

    for row in Request.objects.filter(container_id=settings.CONTAINER_ID):
        r = {"timestamp": str(row.timestamp), "user_agent": row.user_agent}

        this_container_requests.append(r)
    server_ip = str(get_server_ip())

    containers_requests = len(
        Request.objects.filter(container_id=settings.CONTAINER_ID)
    )
    all_requests = len(Request.objects.all())

    context = {
        "container_id": settings.CONTAINER_ID,
        "server_ip": server_ip,
        "requests": reversed(this_container_requests),
        "percentage": round((containers_requests / all_requests) * 100, 1),
    }

    return render(request, "index.html", context=context)

