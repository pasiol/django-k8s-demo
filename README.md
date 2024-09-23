# Django Kubernetes Demo

Simple Django app that calculates the percentage of requests per container. Demonstrates how to run Django in Kubernetes environment.

https://www.djangoproject.com/

The info module creates a UUID for the starting container. /container-info endpoint displays the requests and percentage of total requests received by the container.
![Screenshot](./images/screenshot.png)

The deployment is for Vanilla Kubernetes with local path storage.

https://github.com/pasiol/edunetes

    kubectl apply -f deployments/blue-green/ns.yaml
    kubectl config set-context --current --namespace=blue-green
    kubectl apply -f deployments/blue-green/.
    kubectl get pods -o wide -w
