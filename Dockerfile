FROM pypy:2

RUN useradd -u 1006 -ms /bin/bash rowboat
#RUN mkdir /home/rowboat

ENV PYTHONUNBUFFERED 1
ENV ENV docker

RUN mkdir /opt/rowboat

#ADD requirements.txt /opt/rowboat/
#RUN pip install --prefer-binary -r /opt/rowboat/requirements.txt

WORKDIR /opt/rowboat
