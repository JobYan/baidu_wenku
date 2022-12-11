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

import sys
import wenku_tools
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QFileDialog, QMessageBox

from window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QWidget, self).__init__()
        self.dir = "./"
        self.setupUi(self)
        self.wenku = wenku_tools.wenku()
        self.action_connect()

    def process(self):
        self.wenku.__init__()
        self.wenku.dir = self.dir
        if not self.ldt_link.text():
            QMessageBox.warning(self, "提示", "请填写正确的文库链接")
        else:
            self.wenku.process(self.ldt_link.text())

    def open_dir(self):
        self.dir = QFileDialog.getExistingDirectory(None, '选择保存路径', './')
        self.wenku.dir = self.dir

    def action_connect(self):
        self.btn_download.clicked.connect(self.process)
        self.btn_opendir.clicked.connect(self.open_dir)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sys_window = MainWindow()
    sys_window.show()
    app.processEvents()
    sys.exit(app.exec_())
