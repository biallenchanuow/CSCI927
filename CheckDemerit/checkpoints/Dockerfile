FROM python:3.9
COPY . /checkpointsapp5
COPY requirements.txt /checkpointsapp5/requirements.txt
WORKDIR /checkpointsapp5
RUN pip install -r requirements.txt
# ENTRYPOINT [ "python" ]
# ENV PYTHONPATH ../checkpoints
CMD [ "python", "app.py" ]