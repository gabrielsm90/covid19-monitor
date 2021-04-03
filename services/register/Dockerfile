FROM covid-monitor:latest

ARG SERVER_URL

ENV SERVER_URL=$SERVER_URL

ADD ./services/register ./services/register

RUN pip install -r ./services/register/requirements.txt

ENTRYPOINT python services/register/application
