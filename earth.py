import requests

class Earth:
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
    # 设置会话保存cooike
    session = requests.session()

    # 设置代理
    proxies = {
        "http": "localhost:8888",
        "https": "localhost:8888",
    }

    # 保存图片的地址
    saveDir = ""

    def __init__(self):
        """尚不知道要干哈，传是否开代理、代理设置等，
        专门搞一个函数好一点
        设置如何获取地球图片，做成配置文件更好
        所以没啥用

        看开源requests，基本无类变量，
        都是实例变量。
        于是在这写要用到的变量吧。
        """
        pass

    def setProxies(self):
        """给session设置代理"""
        pass

    def showSessionStatus(self):
        '''查看连接状态，包括cookie、text和headers，
        可选择输出到文本？
        '''
        print(self.session.cookies)
        print()
        pass
    
    def getFixedToken(self):
        """获取迷人的FixedToken放在self.FixedToken备用"""
        # 每天会变的FixedToken，从网页中正则获取
        self.FixedToken = ""
        
        pass

    def getTime(self):
        """获取最新的时间以便在search中填充
        格式:png/Pifd/2022/04-25/10(解释：04-25日期，10是小时)
        """
        pass

    def search(self):
        """搜索当前小时照片
        # 获取策略：
        * 2022年4月25日10:40:51，搜索能搜索一小时的所有图片，每10分钟一张
        由于图片太大，可能要把获取到的图片传到图床
        """
        pass

    def getImageFromHimawari8():
        '''设置图像来源为向日葵8号
        并获取
        图片分辨率：11000 x 11000
        图片大小：正午 144.2 MB 96dpi 24位
        午夜 ： 17.2MB
        '''
        pass

    # def getImageFromFY4A(self):
    #     '''从风云4A获取图像
    #     感觉自动获取有点麻烦
    #     且没有向日葵8号的好看
    #     '''
    #     pass

    def saveImage(self):
        '''保存图片到指定目录
        '''
        pass



if __name__ == "__main__":
    pass
    