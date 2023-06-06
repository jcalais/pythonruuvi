# This script is designed to be called from crontab. 
# It will publish to AWS periodically.
import boto3
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from influxdb import InfluxDBClient

load_dotenv()
TIME_ZONE = os.getenv('TIMEZONE', 0)

def main():
    fivemins_datetime = datetime.now() - timedelta(minutes=5, hours=int(TIME_ZONE))
    fivemins = fivemins_datetime.strftime('%Y-%m-%d %H:%M:%S')
    client = InfluxDBClient(host=os.getenv('INFLUX_HOST'), port=os.getenv('INFLUX_PORT'), database=os.getenv('INFLUX_DB'))
    query = f"select temperature,mac from ruuvi_measurements where time > '{fivemins}' order by time desc limit 20"
    params = {'host': 'server01'}
    
    metrics_data = {}
    result = client.query(query, bind_params=params)
    for row in result:
        if row["mac"] not in metrics_data:
            metrics_data[row["mac"]] = {
                "time": row["time"],
                "temperature": row["temperature"]
            }
    print(metrics_data)

if __name__ == "__main__":
    main()
