# pythonruuvi
A simple solution for collecting ruuvitag data to an Influxdb instance on a Raspberry Pi 3b using Python

## Compatibility and dependencies

* Python 3.6 or higher
* InfluxDb installed and running, configured with a db that you name in the .env file
* Bluetooth configured some way that works with Python library (follow these instructions: https://pypi.org/project/ruuvitag-sensor/)
* There are separate instructions for Raspberry Pi here: https://github.com/ttu/ruuvitag-sensor/blob/master/install_guide_pi.md

## Configuration

Add a .env -file in the root with the following structure:

```
APPROVED_MACS=["AB:CD:EF:12:34:56","12:34:56:AB:CD:EF"]
INFLUX_DB=ruuvi
INFLUX_HOST=localhost
INFLUX_PORT=8086
RUUVI_FIELDMAP=["temperature","humidity","pressure","txPower","movementCounter","measurementSequenceNumber","tagID", "rssi"]
```

Where APPROVED_MACS of course are the mac addresses of your existing ruuvi tags and INFLUX_DB is the name of your database in Influxdb that you wish the data to be written to.

Feel free to edit the default RUUVI_FIELDMAP. It determines what Ruuvi Sensor fields are collected.

## Protip

You can then use Grafana to easily output all this in a nice looking chart.
