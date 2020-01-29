import requests
import json
import time
import datetime

class qd:

    url1 = 'http://47.106.45.249/api/authenticateNew'
    url2 = 'http://47.106.45.249/sign/getMyCheckinSubList'
    url3 = 'http://47.106.45.249:8082/sign/addSignIn'
    token = ""
    dtime = ""
    times = ""


    def __init__(self, username ,password):
        self.username = username
        self.password = password


    def get_token(self):
        datas = {"username": self.password, "password": self.username, "schoolId": "79"}
        r = requests.post(qd.url1, data=datas)
        # print(r.json())

        j = r.json()
        x = j.get("data")
        token = x.get("id_token")
        return token

    def get_time(self):
        # 获取当前时间
        dtime = datetime.datetime.now()
        un_time = time.mktime(dtime.timetuple())
        # print(un_time)

        # 将unix时间戳转换为“当前时间”格式
        times = datetime.datetime.fromtimestamp(un_time)
        return dtime,times

    def sign_in(self):
        data3 = {"time": self.dtime, "ADDR": "广西壮族自治区南宁市西乡塘区上尧街道广西交通运输学校", "AXIS": "22.837773-108.239079", "CONTENT": "",
                 "IDS": "",
                 "ISEVECTION": "0", "SCALE": "18", "authorization": self.token, "token": self.token}
        r = requests.post(self.url3, data=data3)
        return self.times, r.json()

