# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit, QFileDialog
import os
from src.constant.constant import PRE_STEP_BUTTON, GENERATE_BUTTON, CANCEL_BUTTON, CHOOSE_File, WRONG_TITLE, WRONG_PATH, \
    GENERATOR_SETTING_TITLE, GENERATOR_PATH
from src.little_widget.message_box import pop_fail

_author_ = 'luwt'
_date_ = '2020/10/27 15:35'


class GenerateSettingUI:

    def __init__(self, dialog):
        self.parent = dialog
        self._translate = self.parent._translate
        self.setup_ui()

    def setup_ui(self):
        self.widget = QWidget(self.parent.generate_frame)
        self.widget.setObjectName("setting_widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")

        self.label_blank = QLabel(self.widget)
        self.gridLayout.addWidget(self.label_blank, 0, 0, 1, 1)
        self.title = QLabel(self.widget)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 0, 1, 5)
        self.title_blank = QLabel(self.widget)
        self.gridLayout.addWidget(self.title_blank, 2, 0, 1, 1)
        self.path_label = QLabel(self.widget)
        self.path_label.setObjectName('path_label')
        self.gridLayout.addWidget(self.path_label, 3, 0, 1, 1)
        self.path_button = QPushButton(self.widget)
        self.gridLayout.addWidget(self.path_button, 3, 1, 1, 1)
        self.path_value = QLineEdit(self.widget)
        self.gridLayout.addWidget(self.path_value, 3, 2, 1, 3)
        self.path_check = QLabel(self.widget)
        self.path_check.setObjectName("path_check")
        self.gridLayout.addWidget(self.path_check, 4, 2, 1, 3)
        self.blank = QLabel(self.widget)
        self.gridLayout.addWidget(self.blank, 5, 0, 1, 1)

        # 按钮部分
        self.pre_step_button = QPushButton(self.widget)
        self.pre_step_button.setObjectName("pre_step_button")
        self.gridLayout.addWidget(self.pre_step_button, 6, 0, 1, 1)
        self.button_blank = QLabel(self.widget)
        self.button_blank.setObjectName("button_blank")
        self.gridLayout.addWidget(self.button_blank, 6, 1, 1, 1)
        self.button_blank2 = QLabel(self.widget)
        self.button_blank2.setObjectName("button_blank2")
        self.gridLayout.addWidget(self.button_blank2, 6, 2, 1, 1)
        self.generate_button = QPushButton(self.widget)
        self.generate_button.setObjectName("generate_button")
        self.gridLayout.addWidget(self.generate_button, 6, 3, 1, 1)
        self.cancel_button = QPushButton(self.widget)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 6, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        # 按钮点击事件
        self.pre_step_button.clicked.connect(lambda: self.pre_step())
        self.generate_button.clicked.connect(self.generate)
        self.cancel_button.clicked.connect(self.parent.close)

        self.path_button.clicked.connect(self.choose_file)
        self.path_value.textEdited.connect(self.input_text)

        self.retranslateUi()

    def retranslateUi(self):
        self.parent.setWindowTitle(self._translate("Dialog", GENERATOR_SETTING_TITLE))
        self.title.setText(GENERATOR_SETTING_TITLE)
        self.path_label.setText(GENERATOR_PATH)
        self.path_button.setText(CHOOSE_File)
        # 按钮
        self.pre_step_button.setText(PRE_STEP_BUTTON)
        # 生成按钮
        self.generate_button.setText(GENERATE_BUTTON)
        self.generate_button.setDisabled(True)
        self.cancel_button.setText(CANCEL_BUTTON)

    def pre_step(self):
        # 隐藏选择生成器界面
        self.widget.hide()
        # 展示树控件
        self.parent.tree_widget.show()

    def choose_file(self):
        if self.path_value.text():
            start_dir = self.get_existing_dir(self.path_value.text())
        else:
            start_dir = '/'
        filename = QFileDialog.getSaveFileName(self.widget, CHOOSE_File, start_dir, 'Microsoft Word文件 (*.docx)')[0]
        if filename:
            self.path_value.setText(filename)
            self.generate_button.setDisabled(False)

    def input_text(self, text):
        if text:
            self.generate_button.setDisabled(False)
        else:
            self.generate_button.setDisabled(True)

    def get_existing_dir(self, path):
        if os.path.isdir(path):
            return path
        new_path = os.path.split(path)[0]
        if new_path:
            return self.get_existing_dir(new_path)
        else:
            return '/'

    def check_path(self):
        path = self.path_value.text()
        exist_path = self.get_existing_dir(path)
        if exist_path == "/":
            pop_fail(WRONG_TITLE, WRONG_PATH)
            return False
        return True

    def generate(self):
        if self.check_path():
            self.parent.generate(self.path_value.text())

