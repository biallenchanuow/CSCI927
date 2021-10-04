FROM python:3.9 
COPY requirements.txt /appformapp4/requirements.txt
WORKDIR /appformapp4
RUN pip install -r requirements.txt
COPY . /appformapp4
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]