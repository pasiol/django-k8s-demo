# Django Kubernetes Demo

Simple Django app

A simple Django app which calculates the percentage of requests that app has got.

The container info module creates the UUID identifier for the app when it starting up. Every request is saved and also UUID of the app is saved. The URL '/container-info' showing percentage of the requests and listing of all requests, which has the same identifier.

Purpose of the app is learning how the Django app is able to run on Kubernetes cluster. The repository is part of the dev-ops course exercise.

## docker-compose enviroment for debugging

Deploying to Kubernetes cluster is slowly, so I made docker-compose solution for debuggin purposes.

    git clone https://github.com/pasiol/Django-k8s-demo.git
    cd dk8sdemo
    ./buildLocal.sh

## TODO

- Instructions for minikube enviroment
- nginx load balancer

## Remarks

- docker build tries to stat .postgres-volume directory <https://github.com/docker/for-linux/issues/380>