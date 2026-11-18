# Use the official Python runtime; this app needs only the standard library.
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only runtime code, keeping tests and local files out of the image.
COPY --chown=65532:65532 garden_advice.py /app/garden_advice.py

# The console app does not need root privileges, a server or exposed ports.
USER 65532:65532

CMD ["python", "garden_advice.py"]
