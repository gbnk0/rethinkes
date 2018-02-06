FROM python:3.6
COPY * /
RUN mkdir /etc/rethinkes/
COPY config.conf /etc/rethinkes/.
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/entrypoint.sh"]