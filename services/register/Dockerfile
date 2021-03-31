FROM covid-monitor:latest

ARG SERVER_URL

ENV SERVER_URL=$SERVER_URL

ADD ./services/register ./register

RUN pip install -r ./register/requirements.txt

ENTRYPOINT python register/application
