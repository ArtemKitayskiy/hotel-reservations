FROM python:3.10-slim

WORKDIR /app

RUN pip install requests

COPY . .

CMD ["python", "req.py"]

# docker build -t request_service:v1 .
# docker run -d --name request_service_container request_service:v1