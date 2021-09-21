FROM python:3.9 
COPY requirements.txt /applicationapp/requirements.txt
WORKDIR /applicationapp
RUN pip install -r requirements.txt
COPY . /applicationapp
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]