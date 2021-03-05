import requests
import tkinter
import time
import math

url = "http://www.tudbut.de/api"
playTimeUrl = "/getOverallPlaytime"
userRecordUrl = "/getUserRecordByName"


def getOverallPlaytime():
    print("getting pt")
    response = requests.get(str(url + playTimeUrl))
    print("got")
    return response

def getOnlineUsers(delay):
    pt1 = getOverallPlaytime().content
    time.sleep(delay)
    pt2 = getOverallPlaytime().content
    players = math.ceil(int(pt2)-int(pt1))/delay
    return players

def getPlayerData(username):
    response = requests.get(url + userRecordUrl + "?name=" + username)
    response = split(response.text)
    return response

def getUUID(username):
    response = requests.get(url + "/getUUID?name=" + username)
    return response

def getName(UUID):
    response = requests.get(url + "/getName?uuid=" + UUID)
    return response

def split(data):
    list = data.split("\n")
    list2 = []
    for i in list:
        a = i.split(":")
        for b in a:
            list2.append(b)
    it = iter(list2)
    res_dct = dict(zip(it, it))
    return res_dct

def sendLogin(UUID):
    requests.post(url + "/track/login?uuid=" + UUID)

def sendPlay(UUID):
    requests.post(url + "/track/play?uuid=" + UUID)
