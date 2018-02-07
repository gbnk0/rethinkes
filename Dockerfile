FROM python:3.6

COPY * /

RUN apt-get update && apt-get install -yq supervisor
RUN pip3 install -r requirements.txt


RUN mkdir /etc/rethinkes/
COPY config.conf /etc/rethinkes/.
COPY ./etc/supervisord.conf /etc/supervisor/conf.d/rethinkes.conf

CMD /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf