FROM python:3.9 
ENV PYTHONUNBUFFERED 1
WORKDIR /vaccine

COPY requirements.txt /vaccine/requirements.txt
RUN pip install -r requirements.txt
COPY . /vaccine

CMD python -m flask run --host=0.0.0.0