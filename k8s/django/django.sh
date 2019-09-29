kubectl delete -f service.yaml
kubectl delete -f migrate.yaml
kubectl delete -f make_migrations.yaml
kubectl delete -f deployment.yaml
kubectl delete -f secrets.yaml

kubectl create -f secrets.yaml
kubectl create -f deployment.yaml
kubectl create -f make_migrations.yaml
kubectl create -f migrate.yaml
kubectl create -f service.yaml