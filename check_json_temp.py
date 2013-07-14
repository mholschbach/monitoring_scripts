#!/usr/bin/env python
# coding: utf-8
#
# Michael Holschbach
# mholschbach@gmail.com

import argparse, urllib2, json, re

from pprint import pprint

parser = argparse.ArgumentParser(description='Check temperature, humidity or dew point')
parser.add_argument('-H', action="store", dest="hostname", help='Server name')
parser.add_argument('-w', action="store", dest="warn", type=int, help='Warning temperature')
parser.add_argument('-c', action="store", dest="crit", type=int, help='Critical temperature')
parser.add_argument('-temperature', action="store_true", dest="temperature", help='Check temperature')
parser.add_argument('-humidity', action="store_true", dest="humidity", help='Get humidity')
parser.add_argument('-dewpoint', action="store_true", dest="dewpoint", help='Get dew point')
results = parser.parse_args()

if (results.temperature):
    warn = results.warn
    crit = results.crit

    if (warn == None or crit == None):
        print "Warning or critical threshold unset"
        parser.print_help()
        raise SystemExit()

    if (crit <= warn):
        print "Critical must be higher than warning temperature"
        parser.print_help()
        raise SystemExit()

if (results.temperature or results.humidity or results.dewpoint):

    hostname = results.hostname
    try:
        json_page = urllib2.urlopen('http://' + hostname+ '/json')
    except:
        print "Could not connect to " + hostname
        raise SystemExit(3)

else:
    print "Select temperatur, humidity or dew point"
    parser.print_help()
    raise SystemExit()

data = json.load(json_page)
#pprint(data)
json_page.close()

if (results.temperature):
    #print data["Sensor"]["Temperatur"]
    temperature = float(re.sub('.C$', "", data["Sensor"]["Temperatur"]))

if (results.dewpoint):
    #print data["Sensor"]["Taupunkt"]
    dewpoint = float(re.sub('.C$', "", data["Sensor"]["Taupunkt"]))

if (results.humidity):
    #print data["Sensor"]["Feuchtigkeit"]
    humidity = float(re.sub('%', "", data["Sensor"]["Feuchtigkeit"]))

if (results.temperature):
    commonoutput = ": Temperature: " + str(temperature) + " C|Temperature=" + str(temperature)
    commonoutput += ";" + str(warn) + ";" + str(crit)
    if (results.humidity):
        commonoutput += " Humidity=" + str(humidity)
    if (results.dewpoint):
        commonoutput += " DewPoint=" + str(dewpoint)

    if (temperature > crit):
        print "CRITICAL" + commonoutput
        raise SystemExit(2)
    elif (temperature > warn):
        print "WARNING" + commonoutput
        raise SystemExit(1)
    else:
        print "OK" + commonoutput
        raise SystemExit(0)

if (results.dewpoint):
    commonoutput = ": DewPoint: " + str(dewpoint) + " C|DewPoint=" + str(dewpoint)
    if (humidity):
        commonoutput += " Humidity=" + str(humidity)
    #commonoutput += ";" + str(warn) + ";" + str(crit)
    
    #if (dewpoint > crit):
        #print "CRITICAL" + commonoutput
        #raise SystemExit(2)
    #elif (dewpoint > warn):
        #print "WARNING" + commonoutput
        #raise SystemExit(1)
    #else:
    print "OK" + commonoutput
    raise SystemExit(0)

if (results.humidity):
    commonoutput = ": Humidity: " + str(humidity) + " C|Humidity=" + str(humidity)
    
    print "OK" + commonoutput
    raise SystemExit(0)
