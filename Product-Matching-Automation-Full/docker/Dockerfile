
FROM python:3.9
WORKDIR /app
COPY src/ ./src
COPY data/ ./data
RUN pip install -r src/requirements.txt
CMD ["python3", "src/matcher.py"]
