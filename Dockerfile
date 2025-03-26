FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN 
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
