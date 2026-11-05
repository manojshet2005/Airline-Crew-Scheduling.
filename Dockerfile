FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY duty_validator.py .
COPY test_duty_validator.py .

RUN useradd --create-home appuser

USER appuser

CMD ["python", "-m", "pytest", "-v", "-p", "no:cacheprovider", "test_duty_validator.py"]
