FROM python:3.9-slim
WORKDIR /app
RUN pip install flask flask-cors requests pysocks
COPY main.py .
CMD ["python", "main.py"]