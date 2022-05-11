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

Installing Minikube inside the Debian Buster workstation. <https://www.server-world.info/en/note?os=Debian_10&p=kubernetes&f=1>

    minikube start --vm-driver kvm2

Launching the minikube dashboard.

    minikube dashboard

Deploying a Postgres-server into the Minikube cluster.  The issue in initializing Docker image of Postgres 11 in the cluster. May be deployment file is not compatible. Postgres Docker image  9.6.6 working fine.

    kubectl create -f k8s/postgres/volume.yaml
    kubectl create -f k8s/postgres/volume_claim.yaml
    kubectl create -f k8s/postgres/secrets.yaml
    kubectl create -f k8s/postgres/deployment.yaml
    kubectl create -f k8s/postgres/service.yaml

Revealing cluster IP-address for Django service. Put the cluster IP address into Django secrets file.

    minikube ip|base64

Django secrets file.

    apiVersion: v1
    kind: Secret
    metadata:
      name: django-secrets
    type: Opaque
    data:
      clusterip: MTkyLjE2OC4zOS44NQo=

Deploying Django app and migrating changes on the database.

    kubectl create -f k8s/django/secrets.yaml
    kubectl create -f k8s/django/deployment.yaml
    kubectl create -f k8s/django/migrate.yaml
    kubectl create -f k8s/django/service.yaml

Enabling Django service on the Minikube NodePort.

    kubectl get services
    minikube service django-service

## TODO

- Volume for Django.
- nginx load balancer

## Remarks

- docker build-command tries to stat the root only .postgres-volume directory <https://github.com/docker/for-linux/issues/380>

## Links

Installing kustomize

- https://kubectl.docs.kubernetes.io/installation/kustomize/source/
