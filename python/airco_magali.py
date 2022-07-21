from ast import For, operator
from email.utils import parsedate_to_datetime
import json
from src.parser import Parser
from src.models.aircon import Aircon
from src.repository.repository import Repository
from src.utils import Utils
from base64 import b64decode
import time
import datetime

print(str(datetime.datetime.now()) + " - " + "Start execution")
presetTemp = 20
ip = "192.168.10.177"

try:
    print()
    print(str(datetime.datetime.now()) + " - " + ip + " connecting")

    airconStatResponse = Repository.getAirconStats(ip=ip)
    operatorId = airconStatResponse['remoteList'][0]
    aircoUnit = Parser.translateBytes(airconStatResponse['airconStat'])

    # print(json.dumps(aircoUnit.__dict__, sort_keys=False, indent=4))
    if aircoUnit.Operation == True:
        if aircoUnit.PresetTemp < presetTemp:
            # setting temp
            aircoUnit.PresetTemp = presetTemp

            outputJson = Parser.toBase64(airconStat=Utils.convertAirconToAirconStat(aircoUnit))

            response = Parser.translateBytes(Repository.sendAircoCommand(command=outputJson, ip=ip, operatorId=operatorId))
            print(str(datetime.datetime.now()) + " - " + ip + " preset temp set to: " + str(response.PresetTemp))

            # convertedAircon = json.dumps(response.__dict__, sort_keys=False, indent=4)
            # print(convertedAircon)
        else:
            print(str(datetime.datetime.now()) + " - " + ip + " is running at correct preset temp")

    else:
        print(str(datetime.datetime.now()) + " - " + ip + " is not running")
except:
    print(str(datetime.datetime.now()) + " - An exception occured")

print()

