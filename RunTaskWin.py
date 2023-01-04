import os
import sys
import win32api
# from PySide2.QtWidgets import *
from PyQt5.QtWidgets import *
from win_ui import Ui_Form
# 进程管理
class Serve_Window(QWidget):
    def __init__(self):
        # 基本初始化
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("运行新任务")
        # 给需要使用的控件声明好所需函数
        self.ui.run.clicked.connect(self.startp)
        # 浏览文件目录
        self.ui.lookup.clicked.connect(self.lookup)

    def lookup(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择你要运行的文件",  # 标题
            r"data",  # 起始目录
            "(*.*)"  # 选择类型过滤项，过滤内容在括号中 #*.*所有文件
        )
        self.ui.enter.setText(filePath)

    # 运行新任务（新建进程）
    def startp(self):
        task = self.ui.enter.text()
        print(task)
        # 不为空
        if(len(task)!=0 and task.isspace()==False):
            win32api.ShellExecute(0, 'open', task, '', '', 1)
            # 正常执行后退出窗口
            self.close()

    # # 终止进程
    # def killp(self):
    #     task = self.ui.enter.text()
    #     str = "taskkill /pid " + task + " -t -f"
    #     os.system(str)





