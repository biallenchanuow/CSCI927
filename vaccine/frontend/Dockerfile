FROM python:3.9 
COPY requirements.txt /frontapp3/requirements.txt
WORKDIR /frontapp3
RUN pip install -r requirements.txt
COPY . /frontapp3
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]