import os
import logging
from fastapi import FastAPI

# Configuration depuis les variables d'environnement
APP_ENV = os.getenv("APP_ENV", "dev")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

# Configuration du logging (stdout pour Docker/K8s)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

# Initialisation FastAPI
app = FastAPI(title="DevOps Demo API")

logger.info(f"Starting application | env={APP_ENV} | version={APP_VERSION}")


@app.get("/")
def root():
    return {
        "message": "DevOps demo API",
        "env": APP_ENV,
        "version": APP_VERSION,
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {
        "version": APP_VERSION,
        "env": APP_ENV,
    }


@app.get("/hello")
def hello():
    return {"message": "Hello World"}

