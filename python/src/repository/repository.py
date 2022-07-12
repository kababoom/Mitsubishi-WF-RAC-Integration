from ast import Str
from requests import post, Response
import time


class Repository:

    def getAirconStats(ip: str) -> str:
        url = 'http://%s:51443/beaver/command/getAirconStat' % ip
        myobj = {'apiVer': '1.0', 'command': 'getAirconStat', 'deviceId': '1234567890ABCDEF',
                 'operatorId': '8AE05915-C0B5-45FE-A053-B256B408F041', 'timestamp': 1649703587}

        x = post(url, json=myobj)
        # print(x.json()['contents'])
        return x.json()['contents']

    def sendAircoCommand(command: str, ip: str, operatorId: str):
        url = 'http://%s:51443/beaver/command/setAirconStat' % ip
        myobj = {'apiVer': '1.0', 'command': 'setAirconStat', 'contents': {'airconId': 'ec0bae9f398e', 'airconStat': command},
                 'deviceId': 'a68d811862d2ef38', 'operatorId': operatorId, 'timestamp': round(time.time())}

        x = post(url, json=myobj)
        # print(x.json())

        return x.json()['contents']['airconStat']

# b'{"command":"setAirconStat","apiVer":"1.0","operatorId":"d2bc4571-1cea-4858-b0f2-34c18bef1901","deviceId":"a68d811862d2ef38","timestamp":1657622836,"result":2,"contents":{"airconId":"ec0bae9f398e","airconStat":"AAeimqr/AAAAAAASCgAAAAAAAf/////DVIAECBIkkwAAiAAAAgAAAAAAAAOAIJP/gBDS/5QQAwCbsQ==","logStat":0,"updatedBy":"aircon","expires":1657616549,"ledStat":1,"autoHeating":0,"highTemp":"AB","lowTemp":"66","firmType":"WF-RAC","wireless":{"firmVer":"010"},"mcu":{"firmVer":"123"},"timezone":"Europe/Amsterdam","remoteList":["8AE05915-C0B5-45FE-A053-B256B408F041","","",""],"numOfAccount":1}}'
