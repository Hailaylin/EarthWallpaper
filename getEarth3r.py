from requests.packages import urllib3
import requests
import re
import base64

import logging
logging.captureWarnings(True)

urllib3.disable_warnings()

proxies = {
  "http": "localhost:8888",
  "https": "localhost:8888",
}



cookies = {
        'CAKEPHP': '8sbuadntit872ts2htd3uvti8to1htip95o8df7e5dh81lnv93p1',
        '_dd_s': 'logs=1&id=f8954860-373a-4b73-9d44-c0945b305009&created=1650814328832&expire=1650817269513',
    }

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'CAKEPHP=0pvpoq0q26pmgu6m6gq5e0229gv7cvtvvjdgfoec3riio0cg27a0; _dd_s=logs=1&id=c6277094-0314-45fd-a375-86391d5911b7&created=1650804313772&expire=1650806452878',
    'Referer': 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def getFixedToken():
    params = {
        'lang': 'en',
    }
    response = requests.get('https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV',
                            params=params,  headers=headers, verify=False)
    fixedToken = re.findall('var FIXED_TOKEN = "(.*?)";', response.text)[0]
    print("fixedToken = " + fixedToken)


def getImage():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        "Content-Type": "application/x-www-form-urlencoded",
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'CAKEPHP=0pvpoq0q26pmgu6m6gq5e0229gv7cvtvvjdgfoec3riio0cg27a0; _dd_s=logs=1&id=c6277094-0314-45fd-a375-86391d5911b7&created=1650804313772&expire=1650806452878',
        'Referer': 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV?lang=en',
        'Origin': 'https://sc-nc-web.nict.go.jp',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-CSRFToken': '020e1db382162119f2f6e6cf6e7e5e4af311d63c',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        "_method": "POST",
        "data": {
            "FileSearch": {
                "is_compress": "false",
                "fixedToken": "3bd25aaf5254fce7c182b1335cf7a7ccf78daa19",
                "hashUrl": "bDw2maKV",
            }
        },
        "action": "dir_download_dl",
        "filelist": ["/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/2022/04-24/20/hima820220424200000fd.png"],
        "dl_path": "/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/2022/04-24/20/hima820220424200000fd.png"
    }
    from urllib.parse import urlencode

    data = '_method=POST&data%5BFileSearch%5D%5Bis_compress%5D=false&data%5BFileSearch%5D%5BfixedToken%5D=020e1db382162119f2f6e6cf6e7e5e4af311d63c&data%5BFileSearch%5D%5BhashUrl%5D=bDw2maKV&action=dir_download_dl&filelist%5B0%5D=%2Fosn-disk%2Fwebuser%2Fwsdb%2Fshare_directory%2FbDw2maKV%2Fpng%2FPifd%2F2022%2F04-24%2F23%2Fhima820220424233000fd.png&dl_path=%2Fosn-disk%2Fwebuser%2Fwsdb%2Fshare_directory%2FbDw2maKV%2Fpng%2FPifd%2F2022%2F04-24%2F23%2Fhima820220424233000fd.png'

    cookies = {
        'CAKEPHP': '8sbuadntit872ts2htd3uvti8to1htip95o8df7e5dh81lnv93p1',
        '_dd_s': 'logs=1&id=f8954860-373a-4b73-9d44-c0945b305009&created=1650814328832&expire=1650817269513',
    }
    # data = urlencode(data)
    # search = requests.post(url='https://sc-nc-web.nict.go.jp/wsdb_osndisk/fileSearch/search', data='searchPath=png%2FPifd%2F2022%2F04-24%2F23&searchStr=*.png&action=dir_download_dl', verify=False,headers=headers,cookies=cookies)
    # print(search.text)
    response = requests.post('https://sc-nc-web.nict.go.jp/wsdb_osndisk/fileSearch/download',
                            data=data, cookies=cookies,headers=headers, verify=False)
    img = response.content
    filename = 'earth.png'
    with open(filename, 'wb') as f:
        f.write(img)
        print('下载完成')


if __name__ == "__main__":
    getFixedToken()
    # getImage()
    # requests.get("http://baidu.com", proxies=proxies, verify=False)