FROM python:3.9 
COPY requirements.txt /schformapp3/requirements.txt
WORKDIR /schformapp3
RUN pip install -r requirements.txt
COPY . /schformapp3
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]