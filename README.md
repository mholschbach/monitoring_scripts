Nagios/Icinga/Checkmk scripts
==============


### [check_json_temp.py](check_json_temp.py)

Check temperature, humidity, dewpoint provided by a sht11 temperature and humidity sensor from [^1] powered by an ATmega from [^2] on a json web page. I bought and assembled this system in 2007 and it is still working!

```json
{
      "Sensor": {
            "SensorID": "192.168.100.19",
            "Temperatur": "25.7°C",
            "Feuchtigkeit": "55%",
            "Taupunkt": "15.0°C"
      }
}
```
Example:
```console
/usr/local/bin/check_json_temp.py -H <IP> -sensor 0 -w 30 -c 40 -temperature -humidity -dewpoint
OK: Temperature: 25.7 C|Temperature=25.7;30;40 Humidity=55.0 DewPoint=15.0
```

[^1]: https://www.sensirion.com/de/produkte/katalog/SHT11
[^2]: http://tuxgraphics.org/electronics/200709/avr-webserver-sensirion-humidity-temperature.shtml
