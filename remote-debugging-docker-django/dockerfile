FROM python:3.6-alpine
COPY . src/
RUN pip install --no-cache django ptvsd==3.0.0 
EXPOSE 3000 8000
CMD ["python", "src/manage.py", "runserver", "--noreload", "--nothreading", "0.0.0.0:8000"]
