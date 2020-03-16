FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ADD manage.py /code/manage.py
