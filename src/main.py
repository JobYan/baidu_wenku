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

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QFileDialog, QMessageBox

import wenku_tools
from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QWidget, self).__init__()
        self.init_ui()
        self.action_connect()
        self.dir = "./"
        self.wenku = wenku_tools.wenku()

    def init_ui(self):
        self.setupUi(self)
        # pyinstaller打包时，直接将图标放到包里
        # 命令：pyinstaller -F -w -i ./image/logo.ico ./src/main.py
        # self.setWindowIcon(QIcon('./image/icon.ico'))

    def process(self):
        self.wenku.dir = self.dir
        if not self.ldt_link.text():
            QMessageBox.warning(self, "提示", "请填写正确的文库链接")
        else:
            self.wenku.process(self.ldt_link.text())

    def select_dir(self):
        self.dir = QFileDialog.getExistingDirectory(None, '选择保存路径', self.dir)
        self.wenku.dir = self.dir

    def open_dir(self):
        # os.startfile(self.dir)
        if (sys.platform == "win32") or (sys.platform == "linux"):
            os.startfile(self.dir)
        elif sys.platform == "darwin":
            os.system(f"open {self.dir}")

    def action_connect(self):
        self.btn_download.clicked.connect(self.process)
        self.btn_selectdir.clicked.connect(self.select_dir)
        self.btn_opendir.clicked.connect(self.open_dir)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sys_window = MainWindow()
    sys_window.show()
    app.processEvents()
    sys.exit(app.exec_())
