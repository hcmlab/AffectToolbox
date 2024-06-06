from kafka import KafkaProducer
import json
import time

_KAFKA_IP = "127.0.0.1"
_KAFKA_PORT = 9092
kafka_address = _KAFKA_IP + ":" + str(_KAFKA_PORT)
producer = KafkaProducer(bootstrap_servers=kafka_address, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('MessageVSMLog', value='Start_AffectToolBox')

time.sleep(5)