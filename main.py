import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 定义你的URLs
base_url = "http://jwxt.upc.edu.cn/jsxsd/kscj/pscj_list.do?xs0101id=2&jx0404id="
urls = [base_url + str(i) + "&zcj=" for i in range(202320241000001, 202320241009999+1)]

# 定义你的cookies和headers
cookies = {
    "JSESSIONID": "",
    "SERVERID": ""
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Connection": "keep-alive"
}

# 创建一个新的Workbook
wb = Workbook()
ws = wb.active

# 对每个URL发送HTTP请求
valid_urls = 0
for url in urls:
    response = requests.get(url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'dataList'})
    if table:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 3:
                ws.append([url])
                valid_urls += 1

# 检查是否有任何有效的URL
if valid_urls > 0:
    # 保存Workbook到Excel文件中
    wb.save('urls.xlsx')
else:
    print("无满足")