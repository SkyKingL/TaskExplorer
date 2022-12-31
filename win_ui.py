# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 238)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(103, 30, 575, 71))
        self.run = QPushButton(Form)
        self.run.setObjectName(u"run")
        self.run.setGeometry(QRect(467, 141, 93, 28))
        self.lookup = QPushButton(Form)
        self.lookup.setObjectName(u"lookup")
        self.lookup.setGeometry(QRect(583, 141, 93, 28))
        self.enter = QLineEdit(Form)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(133, 100, 541, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(75, 102, 72, 15))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7ba1\u7406\u5668\u5c06\u6839\u636e\u4f60\u6240\u952e\u5165\u7684\u540d\u79f0\uff0c\u4e3a\u4f60\u6253\u5f00\u76f8\u5e94\u7684\u7a0b\u5e8f\u3001\u6587\u4ef6\u5939\u3001\u6587\u6863\u6216 Internet \u8d44\u6e90", None))
        self.run.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c", None))
        self.lookup.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u4e8e\uff1a", None))
    # retranslateUi

