FROM covid-monitor:latest

ADD ./services/scheduler ./services/scheduler

RUN pip install -r ./services/scheduler/requirements.txt

ENTRYPOINT python services/scheduler/application
