# This script is designed to be called from crontab. 
# It will publish to AWS periodically.
import boto3
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from influxdb import InfluxDBClient

load_dotenv()

def main():
    fivemins_datetime = datetime.now() - timedelta(minutes=5)
    fivemins = fivemins_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(fivemins)
    client = InfluxDBClient(host=os.getenv('INFLUX_HOST'), port=os.getenv('INFLUX_PORT'), database=os.getenv('INFLUX_DB'))
    query = f"select temperature,mac from ruuvi_measurements where time > '{fivemins}' limit 20"
    params = {'host': 'server01'}
    result = client.query(query, bind_params=params)
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
