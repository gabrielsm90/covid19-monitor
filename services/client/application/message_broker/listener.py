from services.common.lib.config import Config
from services.common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaConsumer


class CovidNewJobListener(CovidMonitorKafkaConsumer):
    def __init__(self):
        super().__init__(topic=Config.KAFKA_TOPIC_SCHEDULER, group_id="api_client")
