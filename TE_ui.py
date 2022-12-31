# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(726, 765)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.New_Task = QAction(MainWindow)
        self.New_Task.setObjectName(u"New_Task")
        self.Exit = QAction(MainWindow)
        self.Exit.setObjectName(u"Exit")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.Always_Front = QAction(MainWindow)
        self.Always_Front.setObjectName(u"Always_Front")
        self.Fresh = QAction(MainWindow)
        self.Fresh.setObjectName(u"Fresh")
        self.S_Icon = QAction(MainWindow)
        self.S_Icon.setObjectName(u"S_Icon")
        self.full_list = QAction(MainWindow)
        self.full_list.setObjectName(u"full_list")
        self.Shut_Down = QAction(MainWindow)
        self.Shut_Down.setObjectName(u"Shut_Down")
        self.Log_Out = QAction(MainWindow)
        self.Log_Out.setObjectName(u"Log_Out")
        self.About = QAction(MainWindow)
        self.About.setObjectName(u"About")
        self.Fast = QAction(MainWindow)
        self.Fast.setObjectName(u"Fast")
        self.Normal = QAction(MainWindow)
        self.Normal.setObjectName(u"Normal")
        self.Slow = QAction(MainWindow)
        self.Slow.setObjectName(u"Slow")
        self.restart = QAction(MainWindow)
        self.restart.setObjectName(u"restart")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(28, 20, 671, 651))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane{\n"
"min-width:70px;\n"
"min-height:25px;\n"
"border-top: 2px solid;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"\n"
"color: gray;\n"
"\n"
"font:12px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"color: #4796f0;\n"
"\n"
"font:13px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"border-bottom: 2px solid;\n"
"\n"
"border-color: #4796f0;\n"
"\n"
"}")
        self.tabWidget.setUsesScrollButtons(True)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(-7, 10, 691, 571))
        self.tableWidget.setMaximumSize(QSize(1000, 571))
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"QTabWidget::pane{\n"
"min-width:70px;\n"
"min-height:25px;\n"
"border-top: 2px solid;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"\n"
"color: gray;\n"
"\n"
"font:12px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"color: #4796f0;\n"
"\n"
"font:13px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"border-bottom: 2px solid;\n"
"\n"
"border-color: #4796f0;\n"
"\n"
"}")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(115)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableWidget_2 = QTableWidget(self.tab_4)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(0, 0, 691, 581))
        self.tableWidget_2.setStyleSheet(u"QTabWidget::pane{\n"
"min-width:70px;\n"
"min-height:25px;\n"
"border-top: 2px solid;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"\n"
"color: gray;\n"
"\n"
"font:12px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"color: #4796f0;\n"
"\n"
"font:13px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"border-bottom: 2px solid;\n"
"\n"
"border-color: #4796f0;\n"
"\n"
"}")
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(169)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.CPU_record_Plot = PlotWidget(self.tab_3)
        self.CPU_record_Plot.setObjectName(u"CPU_record_Plot")
        self.CPU_record_Plot.setGeometry(QRect(35, 20, 601, 111))
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(35, 0, 91, 16))
        self.GPU_Plot = PlotWidget(self.tab_3)
        self.GPU_Plot.setObjectName(u"GPU_Plot")
        self.GPU_Plot.setGeometry(QRect(36, 213, 601, 111))
        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 190, 91, 16))
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(215, 190, 251, 16))
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(479, 191, 161, 16))
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 394, 101, 16))
        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 491, 101, 16))
        self.sent = QLabel(self.tab_3)
        self.sent.setObjectName(u"sent")
        self.sent.setGeometry(QRect(160, 394, 111, 16))
        self.recv = QLabel(self.tab_3)
        self.recv.setObjectName(u"recv")
        self.recv.setGeometry(QRect(159, 490, 111, 16))
        self.tabWidget.addTab(self.tab_3, "")
        self.P_num = QLabel(self.centralwidget)
        self.P_num.setObjectName(u"P_num")
        self.P_num.setGeometry(QRect(32, 678, 141, 16))
        self.CPU_Use = QLabel(self.centralwidget)
        self.CPU_Use.setObjectName(u"CPU_Use")
        self.CPU_Use.setGeometry(QRect(200, 678, 181, 16))
        self.speed = QLabel(self.centralwidget)
        self.speed.setObjectName(u"speed")
        self.speed.setGeometry(QRect(560, 10, 141, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 726, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_O = QMenu(self.menubar)
        self.menu_O.setObjectName(u"menu_O")
        self.menu_V = QMenu(self.menubar)
        self.menu_V.setObjectName(u"menu_V")
        self.menu_2 = QMenu(self.menu_V)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_U = QMenu(self.menubar)
        self.menu_U.setObjectName(u"menu_U")
        self.menu_H = QMenu(self.menubar)
        self.menu_H.setObjectName(u"menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_O.menuAction())
        self.menubar.addAction(self.menu_V.menuAction())
        self.menubar.addAction(self.menu_U.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())
        self.menu.addAction(self.New_Task)
        self.menu.addAction(self.Exit)
        self.menu_O.addAction(self.Always_Front)
        self.menu_V.addAction(self.Fresh)
        self.menu_V.addAction(self.menu_2.menuAction())
        self.menu_V.addAction(self.S_Icon)
        self.menu_V.addAction(self.full_list)
        self.menu_2.addAction(self.Fast)
        self.menu_2.addAction(self.Normal)
        self.menu_2.addAction(self.Slow)
        self.menu_U.addAction(self.Shut_Down)
        self.menu_U.addAction(self.Log_Out)
        self.menu_H.addAction(self.About)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.New_Task.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u65b0\u4efb\u52a1", None))
        self.Exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7ba1\u7406\u5668", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u8fdb\u7a0b", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u8fdb\u7a0b", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u8fdb\u7a0b", None))
        self.Always_Front.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4e8e\u9876\u5c42", None))
        self.Fresh.setText(QCoreApplication.translate("MainWindow", u"\u7acb\u5373\u5237\u65b0", None))
        self.S_Icon.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u56fe\u6807", None))
        self.full_list.setText(QCoreApplication.translate("MainWindow", u"\u8be6\u7ec6\u5217\u8868", None))
        self.Shut_Down.setText(QCoreApplication.translate("MainWindow", u"\u5173\u673a", None))
        self.Log_Out.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u9500", None))
        self.About.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.Fast.setText(QCoreApplication.translate("MainWindow", u"\u9ad8", None))
        self.Normal.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5e38", None))
        self.Slow.setText(QCoreApplication.translate("MainWindow", u"\u4f4e", None))
        self.restart.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u542f\u7ba1\u7406\u5668", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6620\u50cf\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4f18\u5148\u7ea7", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5b58\u4f7f\u7528", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u7a0b\u6570", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5e94\u7528\u7a0b\u5e8f\u53ca\u8fdb\u7a0b", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d\u79f0", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"CPU", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5b58", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u78c1\u76d8", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u7528\u6237", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CPU\u5229\u7528\u7387(%)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"GPU\u5229\u7528\u7387(%)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5361\u540d\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5b58\u7a7a\u95f2\u7387\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"WLAN\u53d1\u9001\u901f\u7387\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"WLAN\u63a5\u6536\u901f\u7387\uff1a", None))
        self.sent.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.recv.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u6027\u80fd", None))
        self.P_num.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u7a0b\u6570\uff1a", None))
        self.CPU_Use.setText(QCoreApplication.translate("MainWindow", u"CPU \u4f7f\u7528\u7387\uff1a", None))
        self.speed.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u901f\u5ea6:  ", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(F)", None))
        self.menu_O.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879(O)", None))
        self.menu_V.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u770b(V)", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u901f\u5ea6", None))
        self.menu_U.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u673a(U)", None))
        self.menu_H.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(H)", None))
    # retranslateUi

