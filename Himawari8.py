import requests
import re
import urllib3
from urllib.parse import urlencode
import time
import os

class Himawari8:
    """从向日葵8号获取地球图片的所有操作类
    其他获取图片渠道再另外做一个类保存
    因为模拟手动获取的“爬虫”过程
    对每一颗卫星的资源网站都不一样
    避免单个类过于复杂
    进行类层次的拆分

    更好的办法：做一个父类。
    不过得先做出一个实例来，
    看有无必要。
    """
    # 类变量，保存所有操作都要的属性

    def __init__(self):
        """尚不知道要干哈，传是否开代理、代理设置等，
        专门搞一个函数好一点
        设置如何获取地球图片，做成配置文件更好
        所以没啥用

        看开源requests，基本无类变量，
        都是实例变量。
        于是在这写要用到的变量吧。
        """
        
        # 关掉不安全报错
        # https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
        urllib3.disable_warnings()

        # 设置会话保存cooike
        self.session = requests.session()

        # 设置V2ray代理
        self.proxiesV2ray = {
            "http": "localhost:1081",
            "https": "localhost:1081",
        }

        # 设置Fiddler抓包代理
        self.proxiesFiddler = {
            "http": "localhost:8888",
            "https": "localhost:8888",
        }

        # 保存图片的地址
        self.saveDir = "./img/"

        # 设置headers
        self.headers = {
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
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        self.fixedToken = ''
        pass

    def setProxies(self, app:"Fiddler/V2ray") -> None:
        """给session设置代理，可自己设置更多
        参考
        https://docs.python-requests.org/en/latest/user/advanced/#proxies
        """
        if app == "Fiddler":
            proxies = self.proxiesFiddler
        if app == "V2ray":
            proxies = self.proxiesV2ray
        self.session.proxies.update(proxies)

    def setHeaders(self):
        self.session.headers =  self.headers
        pass

    def showSessionStatus(self, msg:"输出会话信息"):
        '''查看连接状态，包括cookie和headers，
        可选择输出到文本？
        '''
        print('\n\t'+msg+'\t')
        print(self.session.cookies)
        print(self.session.cookies.get_dict())
        print(self.session.headers)
        pass

    def showResponse(self, response:"返回体", msg):
        '''看看返回了啥
        args: response -> requests.Response()
        '''
        print('\n  # ' + msg + '\t')
        print(response)
        print(response.text)
        # print(response.headers)
        pass

    def loginGetCookie(self):
        '''这网页要访问三次
        1. GET https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV?lang=en
        返回 Set-Cookie: CAKEPHP=f1tf460v46qkccq1d9pevh979us8l2dqfkodlljh5shillhpv8t0; path=/; secure; HttpOnly
        2. 带着1.返回的Cookie GET https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/login/bDw2maKV?lang=en
        返回 Set-Cookie: CAKEPHP=i0i59tiq3claitdl1l3rjh545o6fjoamuqrg20v014n2uii2j4c0; path=/; secure; HttpOnly
        3. 2.返回的Cookie GET https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV?lang=en
        返回  var FIXED_TOKEN = "b2b03bf510fd89c9e597b0fa21b8bb38803661b3";
        '''
        url = 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV?lang=en'
        url_login = 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/shareDirDownload/login/bDw2maKV?lang=en'
        self.session.headers.update(self.headers)
        response = self.session.get(url, verify=False)
        self.fixedToken = re.findall('var FIXED_TOKEN = "(.*?)";', response.text)[0]
        m = {
            'X-CSRFToken': self.fixedToken,
            'X-Requested-With': 'XMLHttpRequest',}
        self.session.headers.update(m)
        print("登录获取Cookie和fixedToken -> X-CSRFToken = " + self.fixedToken)
        pass
    
    def getTime(self) -> '2022/04-28/10':
        """获取最新的时间以便在search中填充
        格式:png/Pifd/2022/04-25/10(解释：04-25日期，10是小时)
        fd = Full Disk 全盘图
        获取10分钟前时间
        """
        return time.strftime("%Y/%m-%d/%H")
        pass

    def searchPost(self):
        """搜索当前小时照片
        # 获取策略：
        * 2022年4月25日10:40:51，搜索能搜索一小时的所有图片，每10分钟一张
        由于图片太大，可能要把获取到的图片传到图床
        """

        # 数据格式
        data = 'searchPath=png%2FPifd%2F2022%2F04-28%2F10&searchStr=*.png&action=dir_download_dl'

        dataencode = {
            'searchPath' : 'png/Pifd/'+self.getTime(), 
            'searchStr' : '*.png',
            'action' : 'dir_download_dl'
        }

        data = urlencode(dataencode)
        # 测试：没有cookies不给过；没有
        url = 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/fileSearch/search'
        response = self.session.post(url ,data=data, verify=False)
        # self.showResponse(response, "searchPost")
        self.searchResponse = response.json()
        print('检索最新地球影像：')
        print(self.searchResponse)
        pass

    def getFilename(self):
        '''寻找最新的那个文件名
        '''
        self.searchResponse['searchList']
        ['searchList'][len(data['searchList'])-2]
        

    def downloadImage(self) -> str:
        '''下载向日葵8号对地可见光图像
        图片分辨率：11000 x 11000
        图片大小：正午 144.2 MB 96dpi 24位
        午夜 ： 17.2MB

        https://docs.python-requests.org/en/latest/user/advanced/#session-objects
        利用
        with requests.get('https://httpbin.org/get', stream=True) as r:
            # Do things with the response here.
        直接读取stream到文件，避免中转到str中，瞬时多占用150M内存？
        只是避免关闭response而已qaq

        保存也放在这吧，拆得太细，
        保存图片到指定目录 self.saveDir = ""
        '''
        pic_list = self.searchResponse['searchList'][len(self.searchResponse['searchList'])-1]
        filedir = pic_list[4]
        #filedir = "/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/" + self.getTime()+ "/hima8" + "2022 04 24 20 00 00fd.png"
        filename = pic_list[1]
        path = filedir + "/" + filename
        print("远程下载文件名:" + filename)
        print("拍摄地球影像时间："+filename[13:15]+":"+filename[15:17])
        data = {
            "_method": "POST",
            "data[FileSearch][is_compress]": "false",
            "data[FileSearch][fixedToken]": self.fixedToken,
            "data[FileSearch][hashUrl]": "bDw2maKV",
            "action": "dir_download_dl",
            "filelist[0]": path,
            "dl_path": path,
        }

        self.session.headers.update({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})
        url = 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/fileSearch/download'
        with self.session.post(url, stream=True ,data = urlencode(data),verify=False) as r:
            with open(self.saveDir + filename, 'wb') as f:
                f.write(r.content)
        
        size = os.path.getsize(self.saveDir + filename) / 1024.0 / 1024
        print("下载成功！文件大小为:{:.2f}MB".format(size))
        return self.saveDir + filename


if __name__ == "__main__":
    hima = Himawari8()
    hima.loginGetCookie()
    hima.searchPost()
    from wallpaper import Wallpaper
    w = Wallpaper()
    w.earthSmall(hima.downloadImage())
    w.generateBackgroundPic()
    w.setBackgroundPic()

    