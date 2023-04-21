# Jenkins integration with DockerHub and Kubernetes
CI/CD Pipeline for kubernetes deployment using Jenkins

Download Kubernetes Continuous Plugin 1.0 version:
https://updates.jenkins.io/download/plugins/

Add it via Jenkins Dashboard > Manage Jenkins > Plugin Manager > Advanced settings > Choose File

Kubernetes Integeration with Jenkins
go to jenkins > Manage credentials > System ( global) > Add credentials > tkind - Kubernetes configuration ( Kuberconfig)
give id and description
go to kubeconfig > Enter directly
Now you have to copy the content of your kubeconfig file of your cluster. for that -

go to your home directory , you will find  .kube
change your directory to .kube and cat your config file
You will find your kubeconfig like this

apiVersion: v1
clusters:
- cluster:
    certificate-authority:  /home/lana/.minikube/ca.crt
    extensions:
    - extension:
        last-update: Fri, 24 Feb 2023 19:17:00 IST
        provider: minikube.sigs.k8s.io
        version: v1.28.0
      name: cluster_info
    server: https://192.168.49.2:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    extensions:
    - extension:
        last-update: Fri, 24 Feb 2023 19:17:00 IST
        provider: minikube.sigs.k8s.io
        version: v1.28.0
      name: context_info
    namespace: default
    user: minikube
  name: minikube
- context:
    cluster: ""
    namespace: dev
    user: ""
  name: my-context
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: /home/lana/.minikube/profiles/minikube/client.crt
    client-key: home/lana/.minikube/profiles/minikube/client.key
Note : I encoded to base64 the data of ca.crt, client.key and client.crt and directly paste the data instead of /home/lana/.minikube/profiles/minikube/client.crt . But you have to specify the certificate- authority to certificate- authority-data , client-certificate to client-certificate-data, client-key to client-key-data
Now copy the config file data and paste into jenkins > save