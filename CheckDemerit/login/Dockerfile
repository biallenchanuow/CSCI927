FROM python:3.9
COPY . /loginapp5
COPY requirements.txt /loginapp5/requirements.txt
WORKDIR /loginapp5
RUN pip install -r requirements.txt
# ENTRYPOINT [ "python" ]
# ENV PYTHONPATH ../login
CMD [ "python", "app.py" ]
