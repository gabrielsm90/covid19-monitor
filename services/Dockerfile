FROM python:3.8.7-slim

ENV PYTHONPATH=/covid-monitor

RUN mkdir -p /covid-monitor/services

WORKDIR /covid-monitor/services

ADD ./services/common ./common

RUN pip install -r ./common/requirements.txt
