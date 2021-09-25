FROM python:3.9 
COPY requirements.txt /loginapp3/requirements.txt
WORKDIR /loginapp3
RUN pip install -r requirements.txt
COPY . /loginapp3
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]