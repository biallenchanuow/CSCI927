FROM python:3.9 
COPY requirements.txt /appformapp/requirements.txt
WORKDIR /appformapp
RUN pip install -r requirements.txt
COPY . /appformapp
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]