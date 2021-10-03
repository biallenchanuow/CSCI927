FROM python:3.9 
COPY requirements.txt /addre/requirements.txt
WORKDIR /addre
RUN pip install -r requirements.txt
COPY . /addre
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]