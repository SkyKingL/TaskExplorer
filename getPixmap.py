import psutil
from PyQt5.QtGui import QPixmap
from PyQt5.QtWinExtras import QtWin

import win32gui



# function getPixmap
# args: pid(int), large(bool)
#   pid: process id
#   large: return large or small icon handles
# return: PyQt5.QtGui.QPixmap
def getPixmap(pid: int, large=False) -> QPixmap:
    try:
        exe = psutil.Process(pid).cmdline()[0]
        # 使用 win32gui 从进程对应的 exe 文件提取图标
        # large 为大图标句柄列表，small 为小图标句柄列表
        piconLarge, piconSmall = win32gui.ExtractIconEx(exe, 0)
    except:
        return QPixmap("mr.png")

    if large:
        # 没有图标的进程，需要设置个统一的默认图标
        if len(piconLarge) == 0:
            return QPixmap("icon.png")

        # 释放小图标句柄，避免长时间内未释放的图标句柄过多
        for s in piconSmall:
            win32gui.DestroyIcon(s)
        # 获得大图标的QPixmap
        pixmap = QtWin.fromHICON(piconLarge[0])

        # 释放大图标句柄，避免长时间内未释放的图标句柄过多
        for l in piconLarge:
            win32gui.DestroyIcon(l)
        return pixmap
        
    if len(piconSmall) == 0:
        return QPixmap("mr.png")

    # 释放大图标句柄
    for l in piconLarge:
        win32gui.DestroyIcon(l)
    # 获得小图标的QPixmap
    pixmap = QtWin.fromHICON(piconSmall[0])
    # 释放小图标句柄
    for s in piconSmall:
        win32gui.DestroyIcon(s)
    return pixmap