import  requests
# req = requests.get('http://www.baidu.com')
# print(req)
# req.encoding = "utf8"
# content = req.text
# print(content)

while True:
    city = input('请输入城市,回车退出:\n')
    if not city:
        break
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    print(req.text)