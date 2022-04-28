import requests

proxiesFiddler = {
            "http": "localhost:8888",
            "https": "localhost:8888",
        }

cookies = {
    #'_ga': 'GA1.3.1136604875.1650818781',
    'CAKEPHP': 'ontamg5o2oiplqio6bn3j58cvnt0qq85451utltkrbtmohhs2310',
    #'_dd_s': 'logs=1&id=dd6c4f6a-f5c1-42e6-a091-2ef308296779&created=1651113176351&expire=1651114186801',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.3.1136604875.1650818781; CAKEPHP=ontamg5o2oiplqio6bn3j58cvnt0qq85451utltkrbtmohhs2310; _dd_s=logs=1&id=dd6c4f6a-f5c1-42e6-a091-2ef308296779&created=1651113176351&expire=1651114186801',
    'HashToken': 'bDw2maKV',
    'Origin': 'https://sc-nc-web.nict.go.jp',
    'Referer': 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV?lang=en',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
    'X-CSRFToken': 'a8843dace57a6af9c81f8fb5beb8257a59893d7e',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = 'searchPath=png%2FPijp%2F2022%2F04-28%2F10&searchStr=*.png&action=dir_download_dl'

response = requests.post('https://sc-nc-web.nict.go.jp/wsdb_osndisk/fileSearch/search', cookies=cookies, headers=headers, proxies = proxiesFiddler,data=data, verify=False)
print(response.text)