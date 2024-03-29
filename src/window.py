# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(640, 20, 140, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_download = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_download.setFont(font)
        self.btn_download.setObjectName("btn_download")
        self.verticalLayout.addWidget(self.btn_download)
        self.btn_selectdir = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_selectdir.setFont(font)
        self.btn_selectdir.setObjectName("btn_selectdir")
        self.verticalLayout.addWidget(self.btn_selectdir)
        self.btn_opendir = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_opendir.setFont(font)
        self.btn_opendir.setObjectName("btn_opendir")
        self.verticalLayout.addWidget(self.btn_opendir)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 40, 601, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ldt_link = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ldt_link.setFont(font)
        self.ldt_link.setObjectName("ldt_link")
        self.horizontalLayout.addWidget(self.ldt_link)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolBar.setFont(font)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actAbout = QtWidgets.QAction(MainWindow)
        self.actAbout.setObjectName("actAbout")
        self.actHelp = QtWidgets.QAction(MainWindow)
        self.actHelp.setObjectName("actHelp")
        self.toolBar.addAction(self.actAbout)
        self.toolBar.addAction(self.actHelp)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_download.setText(_translate("MainWindow", "开始下载"))
        self.btn_selectdir.setText(_translate("MainWindow", "选择下载路径"))
        self.btn_opendir.setText(_translate("MainWindow", "打开下载路径"))
        self.label.setText(_translate("MainWindow", "文库链接"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actAbout.setText(_translate("MainWindow", "关于"))
        self.actHelp.setText(_translate("MainWindow", "帮助"))
