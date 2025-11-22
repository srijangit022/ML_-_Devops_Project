# ML_+_Devops_Project
I have built a Machine Learning (ML) API and deployed it in a Kubernetes cluster with monitoring and visualization using Prometheus + Grafana.
Machine Learning + DevOps Monitoring Project (End-to-End)

This project demonstrates a complete production-grade ML workflow, deployed using modern DevOps and Kubernetes practices, with full monitoring using Prometheus & Grafana.
It mirrors how real companies deploy, scale, monitor, and maintain Machine Learning applications.

📌 Project Overview

This project builds, deploys, and monitors a Machine Learning prediction API using:

Docker for image packaging

Kubernetes (k8s) for deployment & scaling

Prometheus for metrics scraping

Grafana for visualization and monitoring

kubectl port-forwarding for local cluster access

Optional: Minikube / Docker Desktop Kubernetes as cluster provider

The goal is to show how an ML application behaves in a real microservice environment, similar to how enterprises run ML systems in production.

🧠 Machine Learning Component

The ML part consists of:

✔ A Python ML model (ML app folder)
✔ A FastAPI/Flask REST API
✔ An endpoint like /predict that accepts input and returns ML predictions
✔ Logging & metrics (request count, latency, errors)

These predictions are served through a containerized microservice.

🐳 Docker Containerization

The ML API is packaged into a Docker image using a simple Dockerfile:

Installs dependencies

Copies the ML code

Exposes the API port

Starts the app

This ensures the application runs consistently in any environment.

You build and push the image with:

docker build -t yourname/ml-app .
docker push yourname/ml-app

☸️ Kubernetes Deployment

Kubernetes is used to deploy and manage the ML API using:

Deployment.yaml – controls pods & replicas

Service.yaml – exposes the ML API internally in the cluster

Namespace: monitoring – isolates monitoring tools

This provides:

✔ Auto-restart if a pod fails
✔ Easy scaling (replicas)
✔ Service discovery
✔ Load balancing

You deploy using:

kubectl apply -f k8s/

📡 Prometheus Monitoring Setup

Prometheus monitors the ML API by scraping metrics from:

/metrics


(Flask/FastAPI exports metrics via a library)

Using the Prometheus Operator (kube-prometheus-stack):

helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring


Prometheus automatically detects pods and services via Kubernetes service discovery.

It collects:

API request count

Response time

Pod status

CPU/Memory usage

Error rates

ML API uptime

📊 Grafana Monitoring Dashboard

Grafana visualizes Prometheus metrics.

After installation, you accessed it via port-forward:

kubectl port-forward svc/prometheus-grafana -n monitoring 3000:80


Login:

username: admin

password: (base64 decoded from Kubernetes secret)

Inside Grafana you:

✔ Added Prometheus as a Data Source
✔ Created dashboards showing real-time ML API traffic
✔ Visualized latency, uptime, and performance
✔ Monitored pod health and cluster resources

This mimics real company monitoring setups.

🔍 What the Monitoring Shows

Your dashboards can show:

How many predictions were made

How fast the model responds

If pods are healthy

CPU/Memory usage of pod

How often the API fails

Real time load on the model

This proves you understand ML Observability, which is a major industry skill.

🏗 Architecture Diagram (Text Version)
               ┌─────────────────────────┐
               │   ML Prediction API      │
               │  (FastAPI / Flask app)   │
               └───────────┬─────────────┘
                           │
                    Docker Container
                           │
               ┌───────────▼─────────────┐
               │      Kubernetes          │
               │  Deployment + Service    │
               └───────────┬─────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
Prometheus Server   Grafana Dashboard   K8s Metrics APIs
   (Scrapes)          (Visualizes)          (Pods/Nodes)


⭐ Key Skills Demonstrated

This project shows practical experience with:

🧠 Machine Learning

Building ML models

Creating REST API endpoints

Logging + metrics instrumentation

🧱 DevOps

Docker image creation

Kubernetes deployments

YAML configuration

Service discovery

📈 Monitoring & Observability

Prometheus metrics scraping

Grafana dashboards

K8s pod and cluster monitoring

Troubleshooting 404/connection issues

Base64 decoding of Kubernetes secrets

📦 Cloud-Native Tools

Helm charts

kube-prometheus-stack

Port forwarding

Namespaces & cluster networking

🎯 Why This Project is Valuable

This project is job-ready and demonstrates abilities that companies expect in ML + DevOps candidates:

✔ You deployed an ML model in Kubernetes
✔ You monitored it using Prometheus & Grafana
✔ You debugged DNS, secret, and cluster issues
✔ You integrated ML, DevOps, and Observability — a rare and valuable skill

You can confidently show this in interviews as:

“Real production-style ML deployment with monitoring.”
