
FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /yoyo-weather-app
COPY . ./
RUN pip3 install --upgrade pip
RUN ls .
RUN pip3 install -r requirements.txt
VOLUME /yoyo-weather-app
EXPOSE 8080
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
