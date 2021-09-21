FROM python:3.9 
COPY requirements.txt /scheduleapp/requirements.txt
WORKDIR /scheduleapp
RUN pip install -r requirements.txt
COPY . /scheduleapp
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]