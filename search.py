import requests

cookies = {
    'CAKEPHP': '8sbuadntit872ts2htd3uvti8to1htip95o8df7e5dh81lnv93p1',
    '_dd_s': 'logs=1&id=f8954860-373a-4b73-9d44-c0945b305009&created=1650814328832&expire=1650817269513',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'CAKEPHP=8sbuadntit872ts2htd3uvti8to1htip95o8df7e5dh81lnv93p1; _dd_s=logs=1&id=f8954860-373a-4b73-9d44-c0945b305009&created=1650814328832&expire=1650817269513',
    'HashToken': 'bDw2maKV',
    'Origin': 'https://sc-nc-web.nict.go.jp',
    'Referer': 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV?lang=en',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
    'X-CSRFToken': '020e1db382162119f2f6e6cf6e7e5e4af311d63c',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = 'searchPath=png%2FPifd%2F2022%2F04-24%2F23&searchStr=*.png&action=dir_download_dl'

response = requests.post('https://sc-nc-web.nict.go.jp/wsdb_osndisk/fileSearch/search', cookies=cookies, headers=headers, data=data)
print(response.text)