import os
import sys
import win32api
# from PySide2.QtWidgets import *
from PyQt5.QtWidgets import *
from win_ui import Ui_Form
from common import Va
# 进程管理
class Change_Win(QWidget):
    def __init__(self):
        # 基本初始化
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("切换进程")
        self.ui.label_2.setText("切换至：")
        # 给需要使用的控件声明好所需函数
        self.ui.run.clicked.connect(self.startp)
        # 浏览文件目录
        self.ui.lookup.clicked.connect(self.lookup)

    def lookup(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择你要上传的图片",  # 标题
            r"data",  # 起始目录
            "(*.*)"  # 选择类型过滤项，过滤内容在括号中 #*.*所有文件
        )
        self.ui.enter.setText(filePath)

    # 切换进程——杀死原进程再运行新进程
    # 由于程序未设置路径不合法的异常处理
    # 先运行指定新进程再杀死原进程（指定的新进程有问题就会抛出异常）
    def startp(self):
        task = self.ui.enter.text()
        print(task)
        # 不为空
        if(len(task)!=0 and task.isspace()==False and Va.pid != 1000000):
            win32api.ShellExecute(0, 'open', task, '', '', 1)
            # 防止控制台输出乱码
            os.system("chcp 65001 > nul")
            # taskkill命令强制结束进程
            s = "taskkill /im " + str(Va.pid) + " /f"
            os.system(s)
            Va.pid = 1000000
            # 正常执行后退出窗口
            self.close()