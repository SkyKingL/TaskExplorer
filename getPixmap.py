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
    exe = psutil.Process(pid).cmdline()[0]
    # 使用 win32gui 从进程对应的 exe 文件提取图标
    # large 为大图标句柄列表，small 为小图标句柄列表
    try:
        piconLarge, piconSmall = win32gui.ExtractIconEx(exe, 0)
    except:
        return QPixmap("mr.png")

    if large:
        # 没有图标的进程，需要设置个统一的默认图标
        if len(piconLarge) == 0:
            return QPixmap("icon.png")

        for s in piconSmall:
            win32gui.DestroyIcon(s)
        return QtWin.fromHICON(piconLarge[0])
        
    if len(piconSmall) == 0:
        return QPixmap("mr.png")

    for l in piconLarge:
        win32gui.DestroyIcon(l)
    return QtWin.fromHICON(piconSmall[0])

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QLabel
    import sys, time, pywintypes

    app = QApplication(sys.argv)
    printErr = lambda e, p: print (e, psutil.Process(p).name())

    for pid in psutil.pids():
        try:
            pixmap = getPixmap(pid)
            label = QLabel(None)
            label.setPixmap(pixmap)
            label.resize(960, 720)
        # except (psutil.NoSuchProcess, psutil.AccessDenied, 
        #         psutil.ZombieProcess, IndexError, pywintypes.error) as e:
        #     printErr(e, pid)

        except psutil.NoSuchProcess as e:
            printErr("NoSuchProcess", pid)
        except psutil.AccessDenied as e:
            printErr("AccessDenied", pid)
        except psutil.ZombieProcess as e:
            printErr("ZombieProcess", pid) 
        except IndexError as e:
            printErr("IndexError", pid)
        except pywintypes.error as e:
            printErr(e, pid)