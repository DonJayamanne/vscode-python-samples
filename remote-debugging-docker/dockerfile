FROM python:3.6-alpine
COPY . src/
RUN pip install --no-cache ptvsd
EXPOSE 3000
CMD ["python", "src/sample.py"]
