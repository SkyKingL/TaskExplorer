from common import Va
import time, sys

# 菜单中需要被多个地方调用的方法，或者不需要用到ui控件的方法
class View:
    def SpeedFast(self):
        Va.speed = 1
        print(Va.speed)
    def SpeedNormal(self):
        Va.speed = 2
        print(Va.speed)
    def SpeedSlow(self):
        Va.speed = 3
        print(Va.speed)


        
class File:
    def exitui(self):
        time.sleep(1)
        print('退出管理器...')
        sys.exit()





