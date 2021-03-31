FROM covid-monitor:latest

ADD ./services/scheduler ./scheduler

RUN pip install -r ./scheduler/requirements.txt

ENTRYPOINT python scheduler/application
