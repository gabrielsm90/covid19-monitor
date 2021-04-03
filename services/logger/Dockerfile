FROM covid-monitor:latest

ARG LOG_DIR
ARG LOG_FILE

ENV LOG_DIR=$LOG_DIR \
    LOG_FILE=$LOG_FILE

RUN mkdir -p $LOG_DIR

ADD ./services/logger ./services/logger

ENTRYPOINT python services/logger/application
