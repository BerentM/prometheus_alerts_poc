FROM python:slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install and setup poetry
RUN pip install -U pip \
    && apt-get update && apt-get install -y --no-install-recommends \
    && apt install -y netcat \
    && pip install poetry

WORKDIR /app
COPY . .
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi