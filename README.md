Adicionar repo do spark
```
helm repo add spark-operator https://kubeflow.github.io/spark-operator 
```

Instalar spark operator

```
helm install my-release spark-operator/spark-operator
```

Criar service account spark
```
kubectl create serviceaccount spark
```

Adicionar permissões para o service account

```
kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:spark --namespace=default
```

Rodar spark submit

```
kubectl apply -f .\value.yaml
```