from dotenv import load_dotenv
from ruuvitag_sensor.ruuvi import RuuviTagSensor
from influxdb import InfluxDBClient

load_dotenv()
client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, database=INFLUX_DB)

def handle_data(received_data):
    fields = {}
    mac = received_data[0]
    payload = received_data[1]

    dataFormat = payload['data_format'] if 'data_format' in payload else None
    field_map = RUUVI_FIELDMAP
    for field_label in field_map:
        fields[field_label] = payload[field_label] if field_label in payload else None

    json_body = [
        {
            'measurement': 'ruuvi_measurements',
            'tags': {
                'mac': mac,
                'dataFormat': dataFormat
            },
            'fields': fields
        }
    ]
    client.write_points(json_body)

macs = APPROVED_MACS
RuuviTagSensor.get_datas(handle_data, macs)
