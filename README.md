# Prometheus + Alert manager + API

Basic setup for sending notifications through Prometheus's alert manager.

## Usage

Prerequisite: Docker

Execution:
```bash
docker-compose down -v&&docker-compose up -d --build --remove-orphans&&docker-compose logs -f api
```

Example alert http request body sent to api:
```json
{
  "receiver": "webhook_receiver",
  "status": "firing",
  "alerts": [
    {
      "status": "firing",
      "labels": {
        "alertname": "HighValue",
        "instance": "api:8000",
        "job": "api",
        "severity": "high"
      },
      "annotations": {
        "summary": "poc_metric above 0.5"
      },
      "startsAt": "2022-10-04T13:32:56.014Z",
      "endsAt": "0001-01-01T00:00:00Z",
      "generatorURL": "http://9ef78e326c1f:9090/graph?g0.expr=poc_metric+%3E+0.5&g0.tab=1",
      "fingerprint": "948c667b1fc76492"
    }
  ],
  "groupLabels": {},
  "commonLabels": {
    "alertname": "HighValue",
    "instance": "api:8000",
    "job": "api",
    "severity": "high"
  },
  "commonAnnotations": {
    "summary": "poc_metric above 0.5"
  },
  "externalURL": "http://601cad658ee0:9093",
  "version": "4",
  "groupKey": "{}:{}",
  "truncatedAlerts": 0
}
```


