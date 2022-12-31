from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap
import win32gui
from ctypes import windll
import time
import psutil
from common import Va

class ProcessThread(QObject):
    # 通过类成员对象定义信号
    update_process = pyqtSignal(tuple)
    # 用于每次更新后控制写入行的位置
    # 处理业务逻辑 process
    def run_process(self):
        while True:
            for jci in psutil.pids():
                # windows有一些进程访问权限不够,做个容错处理
                try:
                    process = psutil.Process(jci)
                    a = str(process.name()) # 映像名称
                    b = str(process.pid)    # PID
                    c = str(process.status())   # 状态
                    d = str(process.nice()) # 优先级
                    d = self.ex(d)
                    e = str(round(process.memory_info().rss / 1024. / 1024.,2)) + 'MB' # 内存大小
                    f = str(process.num_threads())  # 线程数
                    x = (a, b, c, d, e, f)
                    self.update_process.emit(x)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            x = ("end", "end")
            self.update_process.emit(x)
            time.sleep(Va.speed)

    def ex(self, d):
        if d == "Priority.ABOVE_NORMAL_PRIORITY_CLASS":
            d = "较高"
        elif d == "Priority.BELOW_NORMAL_PRIORITY_CLASS":
            d = "较低"
        elif d == "Priority.HIGH_PRIORITY_CLASS":
            d = "最高"
        elif d == "Priority.IDLE_PRIORITY_CLASS":
            d = "空闲"
        elif d == "Priority.NORMAL_PRIORITY_CLASS":
            d = "正常"
        elif d == "Priority.PROCESS_MODE_BACKGROUND_BEGIN":
            d = "开始后台模式"
        elif d == "PROCESS_MODE_BACKGROUND_END":
            d = "结束后台模式"
        else:
            d = "实时"
        return d