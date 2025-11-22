# app/app.py
from fastapi import FastAPI, Request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib, os, time, numpy as np

MODEL_PATH = "model.joblib"
app = FastAPI(title="ML-DevOps-Demo")

# Prometheus metrics
REQUESTS = Counter('app_requests_total', 'Total API requests')
LATENCY = Histogram('app_request_latency_seconds', 'Request latency seconds')

def get_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    # Train a tiny model only if missing
    data = load_iris()
    X, y = data.data, data.target
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model

model = get_model()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(payload: dict, request: Request):
    REQUESTS.inc()
    start = time.time()
    values = payload.get("values")
    if not values:
        return {"error": "provide 'values' list e.g. [5.1,3.5,1.4,0.2]"}
    arr = np.array(values).reshape(1, -1)
    pred = model.predict(arr).tolist()
    LATENCY.observe(time.time() - start)
    return {"prediction": pred}

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)
