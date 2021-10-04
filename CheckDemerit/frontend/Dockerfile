FROM python:3.9
COPY . /frontapp5
COPY requirements.txt /frontapp5/requirements.txt
WORKDIR /frontapp5
RUN pip install -r requirements.txt

# ENTRYPOINT [ "python" ]
# ENV PYTHONPATH ../fronend
CMD [ "python", "app.py" ]