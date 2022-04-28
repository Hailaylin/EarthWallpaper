from Himawari8 import Himawari8
from wallpaper import Wallpaper

if __name__ == "__main__":
    hima = Himawari8()
    hima.loginGetCookie()
    hima.searchPost()
    w = Wallpaper()
    w.earthSmall(hima.downloadImage())
    w.generateBackgroundPic()
    w.setBackgroundPic()