FROM python:3.11-slim

WORKDIR /app

RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY app.py .

USER appuser

EXPOSE 8080

CMD ["python", "-u", "app.py"]
