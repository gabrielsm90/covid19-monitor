FROM covid-monitor:latest

ADD ./services/server ./server

RUN pip install -r ./server/requirements.txt

ENTRYPOINT python server/application
