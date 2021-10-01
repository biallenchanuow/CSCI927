FROM python:3.9 
COPY requirements.txt /loginapp4/requirements.txt
WORKDIR /loginapp4
RUN pip install -r requirements.txt
COPY . /loginapp4
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]