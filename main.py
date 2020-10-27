﻿# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import ctypes
from src.main_window.generator_gui import MainWindow
from src.read_qrc.read_file import read_qss
from static import image_rc

import sys


_author_ = 'luwt'
_date_ = '22020/10/27 10:50'


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(
        QtGui.QPixmap(":/boot_jpg/boot.jpg").scaled(600, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    )
    splash.showMessage("加载中...", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
    # 显示启动界面
    splash.show()
    QtWidgets.qApp.processEvents()
    # 获取当前屏幕分辨率
    desktop = QtWidgets.QApplication.desktop()
    app.setStyleSheet(read_qss())
    screen_rect = desktop.screenGeometry()
    ui = MainWindow(screen_rect)
    # 声明AppUserModelID，否则windows认为这是python子程序，无法使用自定义任务栏图标
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("data_dictionary")
    ui.show()
    splash.finish(ui)
    app.exec_()
    ui.close_conn()
    sys.exit()