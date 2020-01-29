import datetime
import time

import requests

url1 = 'http://47.106.45.249/api/authenticateNew'
url2 = 'http://47.106.45.249/sign/getMyCheckinSubList'
url3 = 'http://47.106.45.249:8082/sign/addSignIn'
token = ""
dtime = ""

'''
学号：姓名
171034:xxx
默认密码与账号相同
'''

username = ['171034', '171035', '171030', '171047', '171042']

for use in username:

    print(use)

    # 获取token
    datas = {"username": use, "password": use, "schoolId": "79"}
    r = requests.post(url1, data=datas)
    # print(r.json())
    j = r.json()
    res = j.get("res")

    if res == "succ":
        x = j.get("data")
        token = x.get("id_token")
        # print(x)
        # print(token)
    else:
        print(r.json())

    # 获取当前时间
    dtime = datetime.datetime.now()
    un_time = time.mktime(dtime.timetuple())
    # print(un_time)

    # 将unix时间戳转换为“当前时间”格式
    times = datetime.datetime.fromtimestamp(un_time)

    # 获取签到记录
    # data2 = {"time":dtime,"authorization":token,"token":token}
    # r = requests.post(url2, data=data2)
    # print(r.json())

    data3 = {"time": dtime, "ADDR": "广西壮族自治区南宁市西乡塘区上尧街道广西交通运输学校", "AXIS": "22.837773-108.239079", "CONTENT": "",
             "IDS": "",
             "ISEVECTION": "0", "SCALE": "18", "authorization": token, "token": token}
    r = requests.post(url3, data=data3)
    print(times, r.json())

    time.sleep(2)
