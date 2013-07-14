Nagios scripts
==============


### check_json_temp.py

Check temperature, humidity, dewpoint provided by a sht11 over a json web page on an atmel

json format:
{
  "Sensor": {
		"SensorID": "hostname",
		"Temperatur": "25.5°C",
		"Feuchtigkeit": "58%",
		"Taupunkt": "15.7°C"
	}
}

~ ./check_json_temp.py -H [hostname] -w [warning] -c [critical] -temperature -humidity -dewpoint
WARNING: Temperature: 25.5 C|Temperature=25.5;25;28 Humidity=57.0 DewPoint=15.7


