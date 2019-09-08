FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ADD blogger_search /code/blogger_search
ADD frontend /code/frontend
ADD api /code/api
ADD templates /code/templates
ADD manage.py /code/manage.py
