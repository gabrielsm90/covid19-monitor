FROM covid-monitor:latest

ARG COVID_API_URL

ENV COVID_API_URL=$COVID_API_URL

ADD ./services/client ./client

RUN pip install -r ./client/requirements.txt

ENTRYPOINT python client/application
