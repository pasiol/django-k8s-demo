kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
kubectl delete -f secrets.yaml
kubectl delete -f volume_claim.yaml
kubectl delete -f volume.yaml

kubectl create -f volume.yaml
kubectl create -f volume_claim.yaml
kubectl create -f secrets.yaml
kubectl create -f deployment.yaml
kubectl create -f service.yaml