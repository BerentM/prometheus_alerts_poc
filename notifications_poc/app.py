import random

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Gauge
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_fastapi_instrumentator.metrics import Info

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/v2/alerts")
async def notify_me(data: Request):
    print(await data.json())
    return


def poc_metric():
    METRIC = Gauge(
        "poc_metric",
        "Random number used for AlertManager POC",
    )

    def instrumentation(info: Info) -> None:
        METRIC.set(random.random())

    return instrumentation


prometheus_inst = Instrumentator()
prometheus_inst.add(poc_metric())
prometheus_inst.instrument(app).expose(app)
