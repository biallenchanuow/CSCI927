FROM python:3.9
COPY . /checkpointsapp6
COPY requirements.txt /checkpointsapp6/requirements.txt
WORKDIR /checkpointsapp6
RUN pip install -r requirements.txt
# ENTRYPOINT [ "python" ]
# ENV PYTHONPATH ../checkpoints
CMD [ "python", "app.py" ]