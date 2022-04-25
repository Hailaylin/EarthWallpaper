import PIL.Image as Image
import os
import datetime
import requests
from win32 import win32api, win32gui
import win32con
import time

import himawaripy


import requests
import base64
import json
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
def get_image():
    s = requests.Session()
    url1 = 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV?lang=en'

    cookies = {
        'CAKEPHP': '0pvpoq0q26pmgu6m6gq5e0229gv7cvtvvjdgfoec3riio0cg27a0',
        '_dd_s': 'logs=1&id=c6277094-0314-45fd-a375-86391d5911b7&created=1650804313772&expire=1650806452878',
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

    params = {
        'lang': 'en',
    }

    response = requests.get('https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV', params=params, cookies=cookies, headers=headers)

    #res1 = s.get(url1,headers=headers1).text
    c_token = re.findall('var csrfPreventionSalt = "(.*?)";',response.text)[0]
    print(c_token)
 
    headers2 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length':'0',
        'Host': 'wsswj.hb-n-tax.gov.cn',
        'Origin': 'https://wsswj.hb-n-tax.gov.cn',
        'Referer': 'https://wsswj.hb-n-tax.gov.cn/portal/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'X-CSRF-Token': c_token,
        'X-Requested-With': 'XMLHttpRequest',
        'c-token': c_token,
    }
 
    url2 = '*********************'
    resp = s.post(url=url2,headers=headers2,verify=False)
 
    img = base64.b64decode(json.loads(resp.text)["repData"]['image'])
 
    filename  = 'template.jpg'
    with open('./image/'+filename,'wb') as f:
        f.write(img)
        print('下载完成')
 
get_image()


Images_dir = r'D:\Download'
if not os.path.exists(Images_dir):
    os.makedirs(Images_dir)

count = True



    #合成壁纸图片
    Images_format = '.png'
    zoom = 1
    Image_size = 688
    Image_row = 2
    Image_column = 2
    New_imagepath = Images_dir+'\\compose.png'

    def image_compose():
        to_image = Image.new('RGB',(Image_size*Image_column,Image_size*Image_row))
        for y in range(Image_row):
            for x in range(Image_column):
                Images_path = Images_dir+'\\00'+str(y)+'_00'+str(x)+Images_format
                from_image = Image.open(Images_path).resize((Image_size,Image_size),Image.ANTIALIAS)
                to_image.paste(from_image,(x*Image_size,y*Image_size))
        return to_image.save(New_imagepath)
    try:
        downloadImg()
        image_compose()
        #计算生成的背景图尺寸
        height = int(Image_size*Image_row/0.618)
        width = int(height/9*16)
        to_image = Image.new('RGB',(width,height),(0,0,0))
        from_image = Image.open(New_imagepath)
        to_image.paste(from_image,(int(width/2-Image_size*Image_row/2),int(height*0.382/2)))
        to_image.save(New_imagepath)

        #设置桌面壁纸
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,'Control Panel\\Desktop',0,win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(key,'WallpaperStyle',0,win32con.REG_SZ,'2')
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,New_imagepath,1+2)
        print('成功设置壁纸！')
        time.sleep(60*10)
    finally:
        print('由于网络原因或网站原因未设置壁纸！')
        time.sleep(60*2)
