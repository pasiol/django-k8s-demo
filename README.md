# Django Kubernetes Demo

A simple Django app which calculates the percentage of requests that app has got.

The container info module creates the UUID identifier for the app when it starting up. Every request is saved and also UUID of the app is saved. The URL '/container-info' showing percentage of the requests and listing of all requests, which has the same identifier.

![Screenshot](./screenshot.png)

Purpose of the app is learning how the Django app is able to run on Kubernetes cluster. The repository is part of the dev-ops course exercise.

## docker-compose enviroment for debugging

Deploying to Kubernetes cluster is slowly, so I made 'docker-compose' solution for debugging purposes.

    git clone https://github.com/pasiol/Django-k8s-demo.git
    cd Django-k8s-demo/
    docker-compose build && docker-compose up -d
    docker-compose run web python manage.py migrate --noinput
    firefox http://127.0.0.1:8000 &

Stopping docker-compose

    docker-compose down

## Minikube

Installing into Debian Buster: <https://www.server-world.info/en/note?os=Debian_10&p=kubernetes&f=1>

    minikube start --vm-driver kvm2

Launching dashboard to the minikube.

    minikube dashboard

Deploying a PostgreSQL DB-server to the minikube. Some mystical issue initializing PG 11 image. Seems that PG 9.6.6 working fine.

    kubectl create -f k8s/postgres/volume.yaml
    kubectl create -f k8s/postgres/volume_claim.yaml
    kubectl create -f k8s/postgres/secrets.yaml
    kubectl create -f k8s/postgres/deployment.yaml
    kubectl create -f k8s/postgres/service.yaml

Revealing clusterip in Django service. Putting cluster ip in secret file.

    minikube ip|base64

Put base64 coded ip to Django secret file.

    apiVersion: v1
    kind: Secret
    metadata:
      name: django-secrets
    type: Opaque
    data:
      clusterip: MTkyLjE2OC4zOS44NQo=

Deploying Django and migrating changes.

    kubectl create -f k8s/django/secrets.yaml
    kubectl create -f k8s/django/deployment.yaml
    kubectl create -f k8s/django/migrate.yaml
    kubectl create -f k8s/django/service.yaml

Enabling django-service on the minikube NodePort.

    kubectl get services
    minikube service django-service

## TODO

- Instructions for minikube enviroment
- Own volume for Django, no need to rebuild docker-compose on the small changes.
- nginx load balancer

## Remarks

- docker build tries to stat .postgres-volume directory <https://github.com/docker/for-linux/issues/380>
- Postgres 9.6.6 working in the minikube. Local enviroment Postgres 11 working fine. In minikube initializing database is some issue.
