FROM python:3.8
EXPOSE 8000
ENV PYTHONBUFFERED=1
WORKDIR /usr/scr/app
COPY . /usr/scr/app
RUN pip install -r requirements.txt
CMD [ "python3" ,"manage.py", "runserver", "0.0.0.0:8000" ]