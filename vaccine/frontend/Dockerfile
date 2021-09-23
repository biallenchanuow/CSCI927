FROM python:3.9 
COPY requirements.txt /frontapp/requirements.txt
WORKDIR /frontapp
RUN pip install -r requirements.txt
COPY . /frontapp
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]