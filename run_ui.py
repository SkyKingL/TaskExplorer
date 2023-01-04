from common import *

from TE_ui import Ui_MainWindow
from Menu import View, File

from PyQt5.QtCore import QThread
from Refresh_user import UserThread
from Refresh_Process import ProcessThread
from RunTaskWin import Serve_Window
from ChangePid import Change_Win
from getPixmap import getPixmap
from gpu import gpu

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QBrush
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

import webbrowser
import sys, os

class MainWindow(QMainWindow):
    def __init__(self):
        # 基本初始化
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("王嘉豪阳康了吗")
        # 给需要使用的控件声明好所需函数
        # self.ui.[PushButton名称].clicked.connect([绑定的方法])
        # self.ui.[MenuButton名称].triggered.connect([绑定的方法])
        # 注意这里绑定的是调用的方法，不是方法返回的的结果，所以不能带括号

        # 图标
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

        # 设置窗体大小
        # self.resize(1600, 900)

        # 右键菜单
        # 应用程序及进程 tableWidget 允许右键菜单
        self.ui.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        send_option_1 = QAction(self.ui.tableWidget)
        send_option_1.setText("切换至")
        send_option_1.triggered.connect(self.change_win)  # 点击菜单中的“切换进程”执行的函数

        # 左键点击后获取表格中数据
        self.ui.tableWidget.itemClicked.connect(self.infos)

        send_option_2 = QAction(self.ui.tableWidget)
        send_option_2.setText("结束进程")
        send_option_2.triggered.connect(self.killPid)  # 点击菜单中的“切换进程”执行的函数

        # tableWidget 添加具体的右键菜单
        self.ui.tableWidget.addAction(send_option_1)
        self.ui.tableWidget.addAction(send_option_2)

        Va.speed = 2  # 初始化为正常更新速度

        # 文件(F)——退出管理器
        self.ui.Exit.triggered.connect(File.exitui)
        # 文件(F)——运行新任务
        self.ui.New_Task.triggered.connect(self.serve_win)

        # 查看(V)——立即刷新
        self.ui.Fresh.triggered.connect(self.quick_refresh)

        # 查看(V)——更新速度

        self.ui.Fast.triggered.connect(View.SpeedFast)
        self.ui.Normal.triggered.connect(View.SpeedNormal)
        self.ui.Slow.triggered.connect(View.SpeedSlow)

        # 查看(V)——小图标
        self.ui.S_Icon.triggered.connect(self.S_Icon)

        # 查看(V)——详细列表
        self.ui.full_list.triggered.connect(self.full_list)

        # 选项(O)——置于顶层
        # self.flag 是True——非置顶，是False——置顶
        self.flag = True
        self.ui.Always_Front.triggered.connect(self.show_front)

        # 关机(U)——关机、注销
        self.ui.Shut_Down.triggered.connect(self.guanji)
        self.ui.Log_Out.triggered.connect(self.zhuxiao)

        #帮助(H)——关于
        self.ui.About.triggered.connect(self.openurl)

        # 更新数据
        self.refresh_user()
        self.refresh_process()


    # 小图标
    def S_Icon(self):
        Va.xtb = 1

    # 详细列表
    def full_list(self):
        Va.xtb = 0

    # 关于中说明：左键点击应用程序及进程的表格后再点击右键菜单，才可触发进程管理任务
    # 左键点击后获取参数
    def infos(self, item):
        # item就是点击后传进来的参数
        # 再使用text()函数获取到item里面的文本，这样就可以得到点击的内容了
        self.items = item.text()
        # 过滤出pid列的数据
        if self.items.isdigit() and int(self.items) > 300:
            Va.pid = str(self.items)
        print(self.items)

    # 运行新任务的交互窗口
    def serve_win(self):
        self.form2 = Serve_Window()
        self.form2.show()

    # 运行切换进程的交互窗口
    def change_win(self):
        self.form3 = Change_Win()
        self.form3.show()

    # 终止进程
    def killPid(self):
        if (Va.pid != 1000000):
            # 防止控制台输出乱码
            os.system("chcp 65001 > nul")
            # taskkill命令强制结束进程
            s = "taskkill /im " + str(Va.pid) + " /f"
            os.system(s)
            Va.pid = 1000000

    def show_front(self):
        # 置于顶层
        if(self.flag):
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.flag = False
        # 取消置顶
        else:
            self.setWindowFlags(QtCore.Qt.Widget)
            self.flag = True
        self.show()

    def quick_refresh(self):
        Va.speed = 0.5

    def openurl(self):
        webbrowser.open("https://github.com/SkyKingL/TaskExplorer")

    # 关机——设置弹窗
    def guanji(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("关机")
        msgBox.setText("确定要关机吗？")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No) #默认是No
        ret = msgBox.exec_()
        if ret == QMessageBox.Yes:
            # Save was clicked
            print('确定')
            # 立即关机
            # os.system('shutdown /s /t 0')
        else:
            # cancel was clicked
            print('取消')


    # 注销——设置弹窗
    def zhuxiao(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("注销")
        msgBox.setText("确定要注销吗？")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)  # 默认是No
        ret = msgBox.exec_()
        if ret == QMessageBox.Yes:
            # Save was clicked
            print('确定')
            # 立即注销
            os.system('shutdown /l /t 0')
        else:
            # cancel was clicked
            print('取消')

    # 在def __init__(self)中调用
    def refresh_process(self):
        # 创建线程
        self.backend_1 = ProcessThread()
        # 连接信号
        self.cnt = 0
        self.backend_1.update_process.connect(self.Insert_Process)
        self.thread_1 = QThread()
        self.backend_1.moveToThread(self.thread_1)
        # 开始线程
        self.thread_1.started.connect(self.backend_1.run_process)
        self.thread_1.start()

    # 应用程序及进程页
    def Insert_Process(self, msg):
        processpage = self.ui.tableWidget
        processpage.setRowCount(150)
        j = self.cnt
        #用一个特殊元组表示已经获取所有进程
        if msg[0] == "end":
            # 统计结束，P_Num标签写入进程数
            self.ui.P_num.setText("进程数: " + str(self.cnt))
            self.cnt = 0
            return
        if Va.xtb == 0:
            for i in range(1, 6):
                processpage.setColumnHidden(i, False)
            for i in range(6):
                if i == 0:
                    processpage.setColumnWidth(i, 180)
                else:
                    processpage.setColumnWidth(i, 100)
        else:
            for i in range(1, 6):
                processpage.setColumnHidden(i,True)
            processpage.setColumnWidth(0, 700)

        for i in range(6):

            data = QTableWidgetItem(msg[i]) if i != 0 else \
                   QTableWidgetItem(QIcon(getPixmap(int(msg[1]), large=False)), msg[0])
            
            processpage.setItem(j, i, data)
            # data.setTextColor("green")  # 设置单元格文本颜色
            data.setForeground(QBrush(Qt.GlobalColor.darkGreen))
            data.setTextAlignment(QtCore.Qt.AlignCenter)  # 设置单元格居中
            
        processpage.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)  # 设置表格所有列固定宽度
        processpage.resizeRowsToContents()  # 使行高跟随内容改变
        processpage.verticalHeader().setVisible(False)  # 隐藏垂直标题
        # processpage.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格所有列按比例随窗口自动缩放
        self.cnt = self.cnt + 1

    # 在def __init__(self)中调用
    def refresh_user(self):
        # 创建线程
        self.backend_2 = UserThread()
        # 连接信号
        self.backend_2.update_user.connect(self.Insert_user)
        self.thread_2 = QThread()
        self.backend_2.moveToThread(self.thread_2)
        # 开始线程
        self.thread_2.started.connect(self.backend_2.run_user)
        self.thread_2.start()

    # 用户页
    def Insert_user(self, msg):
        userpage = self.ui.tableWidget_2
        userpage.setRowCount(1)
        for i in range(4):
            data = QTableWidgetItem(msg[i])
            userpage.setItem(0, i, data)
            # data.setTextColor("green")  # 设置单元格文本颜色            
            data.setForeground(QBrush(Qt.GlobalColor.darkGreen))
            
            # CPU使用率标签 需要放在刷新机制中，同时要用已有数据，否则重新读取会有时间差
            if i == 1:
                self.ui.CPU_Use.setText(msg[i])
            if i < 2:
                data.setTextAlignment(QtCore.Qt.AlignCenter)  # 设置单元格居中
            else:
                data.setTextAlignment(QtCore.Qt.AlignLeft)  # 设置单元格左对齐
        userpage.resizeRowsToContents()  # 使行高跟随内容改变
        userpage.verticalHeader().setVisible(False)  # 隐藏垂直标题
        userpage.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格所有列按比例随窗口自动缩放

        if Va.speed != 0.5:
            Va.lastspeed = Va.speed # 记录上一次不是立即刷新的速度，同时保证已经刷新过
        elif Va.speed == 0.5 and Va.speedflag ==0:
            Va.speedflag = 1 #如果是立即刷新对应的速度，这次刷新执行后就可以将速度调整回来
            return
        elif Va.speed == 0.5 and Va.speedflag == 1:
            Va.speed = Va.lastspeed
            Va.speedflag = 0

        # 把“更新速度”标签也更新
        if Va.speed == 1:
            Va.gx = "高"
        elif Va.speed == 2:
            Va.gx = "正常"
        elif Va.speed == 3:
            Va.gx = "低"
        self.ui.speed.setText("更新速度：" + Va.gx)

        # 画性能图 在绘图控件中绘制图形
        self.ui.CPU_record_Plot.plot(Va.cpu_data)

        self.ui.label_2.setText("显卡名：" + gpu.gpu_name)
        self.ui.label_3.setText("显存空闲率：" + str(round(gpu.memery_info.free / gpu.memery_info.total * 100, 2)) + '%')
        self.ui.GPU_Plot.plot(Va.gpu_data)

        self.ui.sent.setText(str(round(Va.bytes_sent, 2)) + " KB/s")
        self.ui.recv.setText(str(round(Va.bytes_recv, 2)) + " KB/s")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec_())