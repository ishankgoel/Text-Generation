FROM python:3.7
#RUN apt add --update python py-pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY txtgen /src/txtgen
EXPOSE 5000
WORKDIR /src
CMD uvicorn app:app --reload --host 0.0.0.0 --port 5000