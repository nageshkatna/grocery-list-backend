# docker/Dockerfile
FROM python:3.10.12

RUN apt-get update && apt-get install -y netcat-openbsd

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080

WORKDIR /app

# Copy requirements from project root
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Copy entrypoint script from docker/
COPY docker/docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# Copy Django app code from project root
COPY . /app

EXPOSE 8080

ENTRYPOINT ["/app/docker-entrypoint.sh"]