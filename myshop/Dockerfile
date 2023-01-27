FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
