FROM python:3.13.1-bookworm

RUN mkdir -p /code/django

COPY requirements.txt /code

RUN pip install --no-cache-dir -r /code/requirements.txt

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
