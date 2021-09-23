FROM python:3.9 
COPY requirements.txt /schformapp/requirements.txt
WORKDIR /schformapp
RUN pip install -r requirements.txt
COPY . /schformapp
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]