FROM python:3.11-slim

WORKDIR /ml_service
COPY . /ml_service/

VOLUME ["/models"]

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t ml_service:v1 .
# docker run -d -p 8000:8000 -v $(pwd)/../models:/models --name ml_service_container ml_service:v1