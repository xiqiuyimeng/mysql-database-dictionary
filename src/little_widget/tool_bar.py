﻿# -*- coding: utf-8 -*-
"""
工具栏
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from src.func.tree_function import add_conn_func

_author_ = 'luwt'
_date_ = '2020/10/27 10:50'


def fill_tool_bar(gui):
    add_insert_conn_tool(gui)
    add_refresh_tool(gui)
    add_generate_tool(gui)
    add_clear_tool(gui)
    add_exit_tool(gui)


def add_insert_conn_tool(gui):
    # 指定图标
    insert_tool = QAction(QIcon(':/icon/add.png'), '添加连接', gui)
    insert_tool.setStatusTip('在左侧列表中添加一条连接')
    insert_tool.triggered.connect(lambda: add_conn_func(gui, gui.screen_rect))
    gui.toolBar.addAction(insert_tool)


def add_refresh_tool(gui):
    refresh_tool = QAction(QIcon(':/icon/refresh.png'), '刷新', gui)
    refresh_tool.setStatusTip('刷新')
    refresh_tool.setShortcut('F5')
    refresh_tool.triggered.connect(gui.refresh)
    gui.toolBar.addAction(refresh_tool)


def add_generate_tool(gui):
    generate_tool = QAction(QIcon(':/icon/exec.png'), '生成', gui)
    generate_tool.setStatusTip('根据选择执行生成命令')
    generate_tool.triggered.connect(gui.generate)
    gui.toolBar.addAction(generate_tool)


def add_clear_tool(gui):
    clear_tool = QAction(QIcon(':/icon/remove.png'), '清空选择', gui)
    clear_tool.setStatusTip('清空所有已经选择的字段')
    clear_tool.triggered.connect(gui.clear_selected)
    gui.toolBar.addSeparator()
    gui.toolBar.addAction(clear_tool)


def add_exit_tool(gui):
    exit_tool = QAction(QIcon(':/icon/exit.png'), '退出程序', gui)
    exit_tool.setStatusTip('退出应用程序')
    exit_tool.triggered.connect(gui.close)
    gui.toolBar.addSeparator()
    gui.toolBar.addAction(exit_tool)
