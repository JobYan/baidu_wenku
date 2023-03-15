#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * @Author       : JobYan
 * @Email        : jobyan@foxmail.com
 * @Date         : 2022-11-25 15:15:51
 * @LastEditors  : JobYan
 * @LastEditTime : 2022-11-26 14:38:32
 * @FilePath     : /main.py
 * @Description  :
"""

import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QFileDialog, QMessageBox

import wenku_tools
from window import Ui_MainWindow
import window_about
import window_help


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QWidget, self).__init__()
        self.init_ui()
        self.setFixedSize(self.width(), self.height())  # 固定窗口大小
        self.action_connect()
        self.dir = "./"
        self.wenku = wenku_tools.wenku()

    def init_ui(self):
        self.setupUi(self)
        self.statusBar().showMessage("欢迎使用文库文档下载软件，请填写文档链接，并点击'开始下载'按钮")
        self.setWindowTitle("文库文档下载软件")
        # pyinstaller打包时，直接将图标放到包里
        # 命令：pyinstaller -F -w -i ./image/logo.ico ./src/main.py
        # self.setWindowIcon(QIcon("./image/icon.ico"))

    def process(self):
        try:
            self.wenku.dir = self.dir
            if not self.ldt_link.text():
                self.statusBar().showMessage("提示信息：文档链接无效，请检查文档链接是否有误")
                QMessageBox.warning(self, "提示", "请检查文档链接是否有误")
            else:
                self.statusBar().showMessage("提示信息：文档正在下载，请稍后")
                self.wenku.process(self.ldt_link.text())
                self.statusBar().showMessage("提示信息：文档下载成功，请在保存路径中查找文档")
        except:
            self.statusBar().showMessage("提示信息：文档链接无效，请检查文档链接是否有误")
            QMessageBox.warning(self, "提示", "请检查文档链接是否有误")

    def select_dir(self):
        self.statusBar().showMessage("提示信息：请选择文档保存路径")
        save_dir = QFileDialog.getExistingDirectory(None, "请选择保存路径", self.dir)
        if save_dir:
            self.wenku.dir = save_dir
            self.dir = save_dir
            self.statusBar().showMessage(f"提示信息：文件将保存在 {save_dir}")
        else:
            self.statusBar().showMessage("提示信息：文件将保存在本程序所在路径")

    def open_dir(self):
        # os.startfile(self.dir)
        self.statusBar().showMessage("提示信息：正在打开文件保存路径")
        if (sys.platform == "win32") or (sys.platform == "linux"):
            os.startfile(self.dir)
        elif sys.platform == "darwin":
            os.system(f"open {self.dir}")
        self.statusBar().showMessage("提示信息：文件保存路径已打开")

    def show_about(self):
        about_window.show()
        about_window.setFocus()

    def show_help(self):
        help_window.show()
        help_window.setFocus()

    def action_connect(self):
        self.btn_download.clicked.connect(self.process)
        self.btn_selectdir.clicked.connect(self.select_dir)
        self.btn_opendir.clicked.connect(self.open_dir)
        self.actAbout.triggered.connect(self.show_about)
        self.actHelp.triggered.connect(self.show_help)


class AboutWindow(QMainWindow, window_about.Ui_MainWindow):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # 固定窗口大小
        self.setFocusPolicy(QtCore.Qt.ClickFocus)

    def focusOutEvent(self, QFocusEvent):
        # 重写失去焦点事件
        self.close()


class HelpWindow(QMainWindow, window_help.Ui_MainWindow):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # 固定窗口大小
        self.setFocusPolicy(QtCore.Qt.ClickFocus)

    def focusOutEvent(self, QFocusEvent):
        # 重写失去焦点事件
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sys_window = MainWindow()
    about_window = AboutWindow()
    help_window = HelpWindow()
    sys_window.show()
    app.processEvents()
    sys.exit(app.exec_())
