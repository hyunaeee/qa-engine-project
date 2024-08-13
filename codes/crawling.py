import requests
from bs4 import BeautifulSoup

url = "https://glaw.scourt.go.kr/wsjo/panre/sjo100.do?contId=3258944"
# url = "https://glaw.scourt.go.kr/wsjo/panre/sjo060.do#1723514994454"
# https://glaw.scourt.go.kr/wsjo/panre/sjo060.do#1723515018946
# https://glaw.scourt.go.kr/wsjo/panre/sjo060.do#1723515038629
# https://glaw.scourt.go.kr/wsjo/panre/sjo060.do#1723515052814
# https://glaw.scourt.go.kr/wsjo/panre/sjo060.do#1723515066590
# https://glaw.scourt.go.kr/wsjo/panre/sjo060.do#1723515078344


res = requests.get(url=url)
bs = BeautifulSoup(res.text, "html.parser")

print(bs)

