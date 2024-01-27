FROM python:3.10.12-slim-bullseye
RUN mkdir build
WORKDIR /build
COPY app app
COPY routes routes
COPY static static
COPY requirements.txt .
RUN pip install --no-cache-dir  -r requirements.txt
EXPOSE 80
CMD python -m uvicorn app.main:app --host 0.0.0.0 --port 80 --log-config config/logging.conf