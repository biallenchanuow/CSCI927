FROM python:3.9 
COPY requirements.txt /frontapp4/requirements.txt
WORKDIR /frontapp4
RUN pip install -r requirements.txt
COPY . /frontapp4
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]