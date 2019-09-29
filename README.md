# Django Kubernetes Demo

A simple Django app which calculates the percentage of requests that app has got.

The container info module creates the UUID identifier for the app when it starting up. Every request is saved and also UUID of the app is saved. The URL '/container-info' showing percentage of the requests and listing of all requests, which has the same identifier.

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

    minikube ip|base64

    apiVersion: v1
    kind: Secret
    metadata:
      name: django-secrets
    type: Opaque
    data:
      clusterip: MTkyLjE2OC4zOS44NQo=

    kubectl create -f secrets.yaml

    


## TODO

- Instructions for minikube enviroment
- Own volume for Django, no need to rebuild docker-compose on the small changes.
- nginx load balancer

## Remarks

- docker build tries to stat .postgres-volume directory <https://github.com/docker/for-linux/issues/380>