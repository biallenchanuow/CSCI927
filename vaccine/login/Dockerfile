FROM python:3.9 
COPY requirements.txt /loginapp/requirements.txt
WORKDIR /loginapp
RUN pip install -r requirements.txt
COPY . /loginapp
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]