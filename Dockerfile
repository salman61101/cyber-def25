FROM python:3.10-slim

WORKDIR /app

COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

COPY model.pkl .
COPY inference.py .

RUN mkdir -p /input/logs && mkdir -p /output

ENV INPUT_DIR=/input/logs
ENV OUTPUT_DIR=/output

CMD ["python", "inference.py"]
