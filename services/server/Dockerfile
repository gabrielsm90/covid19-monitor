FROM covid-monitor:latest

ADD ./services/server ./services/server

RUN pip install -r ./services/server/requirements.txt

ENTRYPOINT python services/server/application
