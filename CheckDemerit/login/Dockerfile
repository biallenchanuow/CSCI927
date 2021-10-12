FROM python:3.9
COPY . /loginapp6
COPY requirements.txt /loginapp6/requirements.txt
WORKDIR /loginapp6
RUN pip install -r requirements.txt
# ENTRYPOINT [ "python" ]
# ENV PYTHONPATH ../login
CMD [ "python", "app.py" ]
