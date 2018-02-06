FROM python:3.6
COPY * /
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/entrypoint.sh"]