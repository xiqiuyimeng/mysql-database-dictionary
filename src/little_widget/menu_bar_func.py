﻿# -*- coding: utf-8 -*-
"""
菜单栏列表生成
"""

from PyQt5 import QtGui, QtWidgets

from src.constant.constant import ADD_CONN_MENU, GENERATE_MENU, FILE_MENU, EXIT_MENU
from src.func.tree_function import add_conn_func

_author_ = 'luwt'
_date_ = '2020/10/27 10:50'


def fill_menu_bar(gui):
    """
    填充菜单栏
    :param gui: 启动的主窗口界面对象
    """
    gui.file_menu = gui.menubar.addMenu(FILE_MENU)
    gui.file_menu.setObjectName("file_menu")
    add_conn_menu(gui)
    generate_menu(gui)
    exit_app_menu(gui)


def add_conn_menu(gui):
    """
    添加连接菜单
    :param gui: 启动的主窗口界面对象
    """
    add_action = QtWidgets.QAction(QtGui.QIcon(':/icon/add.png'), ADD_CONN_MENU, gui)
    add_action.setShortcut('Ctrl+N')
    add_action.setStatusTip('在左侧列表中添加一条连接')
    add_action.triggered.connect(lambda: add_conn_func(gui, gui.screen_rect))

    gui.file_menu.addAction(add_action)


def exit_app_menu(gui):
    """
    退出菜单
    :param gui: 启动的主窗口界面对象
    """
    exit_action = QtWidgets.QAction(QtGui.QIcon(':/icon/exit.png'), EXIT_MENU, gui)
    exit_action.setShortcut('Ctrl+Q')
    exit_action.setStatusTip('退出应用程序')
    exit_action.triggered.connect(gui.close)

    gui.file_menu.addAction(exit_action)


def generate_menu(gui):
    """
    生成菜单
    :param gui: 启动的主窗口界面对象
    """
    generate_action = QtWidgets.QAction(QtGui.QIcon(':/icon/exec.png'), GENERATE_MENU, gui)
    generate_action.setShortcut('Ctrl+G')
    generate_action.setStatusTip('根据选择执行生成命令')
    generate_action.triggered.connect(gui.generate)

    gui.file_menu.addAction(generate_action)
