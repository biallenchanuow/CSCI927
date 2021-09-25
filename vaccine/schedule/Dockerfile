FROM python:3.9 
COPY requirements.txt /schformapp4/requirements.txt
WORKDIR /schformapp4
RUN pip install -r requirements.txt
COPY . /schformapp4
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]