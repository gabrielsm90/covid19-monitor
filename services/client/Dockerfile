FROM covid-monitor:latest

ARG COVID_API_URL

ENV COVID_API_URL=$COVID_API_URL

ADD ./services/client ./services/client

RUN pip install -r ./services/client/requirements.txt

ENTRYPOINT python services/client/application
