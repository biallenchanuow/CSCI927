FROM python:3.9 
COPY requirements.txt /appformapp3/requirements.txt
WORKDIR /appformapp3
RUN pip install -r requirements.txt
COPY . /appformapp3
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]