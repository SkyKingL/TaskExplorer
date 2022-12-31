from common import *
import getpass, psutil, time
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from gpu import gpu

class UserThread(QObject):
    # 通过类成员对象定义信号
    update_user = pyqtSignal(tuple)

    # 处理业务逻辑 user
    def run_user(self):
        while True:
            usep = psutil.cpu_percent(interval=1)

            Va.cpu_data.append(usep)
            Va.gpu_data.append(gpu.gpu_memory_rate)

            key_info, net_in, net_out = self.get_rate(self.get_key)

            for key in key_info:
                # 获取WLAN的网络信息即可
                if key == 'WLAN':
                    Va.bytes_sent = round(net_in.get(key), 2)
                    Va.bytes_recv = round(net_out.get(key), 2)

            a = str(getpass.getuser())

            b = ' cpu 使⽤率：' + str(usep) + '%'
            mem = psutil.virtual_memory()
            mewrate = float(mem.used / mem.total)
            c = ' 总体内存：' + str(round(mem.total / 1024.0 / 1024.0 / 1024.0, 2)) + \
                'G\n 使⽤内存：' + str(round(mem.used / 1024.0 / 1024.0 / 1024.0, 2)) + \
                'G\n 空闲内存：' + str(round(mem.free / 1024.0 / 1024.0 / 1024.0, 2)) + \
                'G\n 使⽤率：' + str(round(mewrate * 100, 1)) + '%'
            d = ' 硬盘使⽤率：' + str(round(psutil.disk_usage('/').percent, 1)) + \
                '%\n 剩余容量：' + str(round(psutil.disk_usage('/').free / 1024.0 / 1024.0 / 1024.0, 2)) + \
                'G\n 使⽤容量：' + str(round(psutil.disk_usage('/').used / 1024.0 / 1024.0 / 1024.0, 2)) + \
                'G\n 总容量：' + str(round(psutil.disk_usage('/').total / 1024.0 / 1024.0 / 1024.0, 2)) + 'G'

            x = (a, b, c, d)
            self.update_user.emit(x)
            time.sleep(Va.speed)

    def get_key(self):
        key_info = psutil.net_io_counters(pernic=True).keys()  # 获取网卡名称

        recv = {}
        sent = {}

        for key in key_info:
            recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)  # 各网卡接收的字节数
            sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)  # 各网卡发送的字节数

        return key_info, recv, sent

    # 函数计算每秒速率
    def get_rate(self, func):
        import time

        key_info, old_recv, old_sent = func()  # 上一秒收集的数据

        time.sleep(1)

        key_info, now_recv, now_sent = func()  # 当前所收集的数据

        net_in = {}
        net_out = {}

        for key in key_info:
            net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)  # 每秒接收速率
            net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024)  # 每秒发送速率

        return key_info, net_in, net_out



