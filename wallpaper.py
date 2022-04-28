from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
import ctypes


class Wallpaper:
    '''进行壁纸的操作
    '''

    def __init__(self):
        self.backgroundPath = 'D:/Project/getEarthPic/background.png'
        self.screen_w = 3840
        self.screen_h = 2160
        self.earth_resize_path = 'earth_'+str(self.screen_h)+'.png'

    def earthSmall(self, img_path:'path或file object'):
        # self.earth_img_path = img_path
        bigEarth = Image.open(img_path)
        earthSize = self.screen_h,self.screen_h
        smallEarth = bigEarth.resize(earthSize)
        smallEarth.save(self.earth_resize_path)
        print('保存调整图像', self.screen_h,'到', self.earth_resize_path)
    
    def generateBackgroundPic(self):
        '''生成背景图片
        
        '''
        blackImg = Image.new('RGBA', (self.screen_w, self.screen_h), 'Black')
        # blackImg = ImageDraw.Draw(blackImg)
        smallEarth = Image.open(self.earth_resize_path)
        blackImg.paste(smallEarth, (int((self.screen_w - self.screen_h)/2),0))
        blackImg.save('background.png')
        print('背景图保存到'+'background.png')

    def setBackgroundPic(self):
        '''设置背景图片
        '''
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.backgroundPath, 0)
        print('设置成功')


if __name__ == "__main__":
    w = Wallpaper()
    w.generateBackgroundPic()
    w.setBackgroundPic()
    pass