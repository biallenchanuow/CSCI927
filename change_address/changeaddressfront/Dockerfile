FROM python:3.9 
COPY requirements.txt /addfront/requirements.txt
WORKDIR /addfront
RUN pip install -r requirements.txt
COPY . /addfront
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]