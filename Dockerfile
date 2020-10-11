FROM python:2.7.17

RUN useradd -u 1006 -ms /bin/bash rowboat

ENV PYTHONUNBUFFERED 1
ENV ENV docker

RUN mkdir /opt/rowboat

ADD requirements.txt /opt/rowboat/
RUN pip install -r /opt/rowboat/requirements.txt

WORKDIR /opt/rowboat
