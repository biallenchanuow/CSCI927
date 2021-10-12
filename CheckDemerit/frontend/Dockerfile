FROM python:3.9
COPY . /frontapp6
COPY requirements.txt /frontapp6/requirements.txt
WORKDIR /frontapp6
RUN pip install -r requirements.txt

# ENTRYPOINT [ "python" ]
# ENV PYTHONPATH ../fronend
CMD [ "python", "app.py" ]