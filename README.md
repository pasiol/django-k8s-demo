# Django Kubernetes Demo

A simple Django app which calculates the percentage of requests per container.

The info module creates the UUID for the starting container. /container-info endpoint displays the requests and percentage of total requests received by the container.
![Screenshot](./screenshot.png)

## docker-compose enviroment for debugging

Deploying to Kubernetes cluster is slowly, so I made 'docker-compose' solution for debugging purposes.

    git clone https://github.com/pasiol/Django-k8s-demo.git
    cd Django-k8s-demo/
    docker-compose build && docker-compose up -d
    docker-compose run web python manage.py migrate --noinput
    firefox http://127.0.0.1:8000 &

Stopping docker-compose

    docker-compose down

## deployment on the local k8s dev environment

TODO

## Links

Installing kustomize

- https://kubectl.docs.kubernetes.io/installation/kustomize/source/
