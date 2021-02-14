# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from css.tool_css import Qss


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 540)
        MainWindow.setMaximumSize(640, 540)
        MainWindow.setMinimumSize(640, 540)
        MainWindow.move(500, 200)
        self.q_icon = QtGui.QIcon("D:/data/develop/idea-project/python/my-tool/image/face.jpg")
        MainWindow.setWindowIcon(self.q_icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建一个窗口页
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(20, 4, 604, 500)
        self.tabWidget.setObjectName("tabWidget")

        # # 测试，看看界面效果
        # self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        # self.tabWidget_2.setGeometry(20, 220, 300, 200)
        # self.tabWidget_2.setObjectName("tabWidget")

        # 大窗口里边添加子窗口
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.q_group_box = QtWidgets.QGroupBox(self.tab_1)
        self.q_group_box.setGeometry(QtCore.QRect(9, 9, 580, 450))
        self.q_group_box.setObjectName("q_group_box")

        self.q_label_1 = QtWidgets.QLabel(self.q_group_box)
        self.q_label_1.setGeometry(QtCore.QRect(40, 40, 60, 24))
        self.q_label_1.setObjectName("q_label_1")

        self.q_line_edit = QtWidgets.QLineEdit(self.q_group_box)
        self.q_line_edit.setGeometry(QtCore.QRect(102, 40, 160, 24))
        self.q_group_box.setObjectName("q_line_edit")

        self.q_push_button = QtWidgets.QPushButton(self.q_group_box)
        self.q_push_button.setGeometry(40, 80, 60, 24)
        self.q_push_button.setObjectName("q_push_button")
        self.q_push_button.setIcon(self.q_icon)

        self.q_label_2 = QtWidgets.QLabel(self.q_group_box)
        self.q_label_2.setGeometry(QtCore.QRect(165, 80, 60, 24))
        self.q_label_2.setObjectName("q_label_2")

        # 添加进度条
        self.q_progress_bar = QtWidgets.QProgressBar(self.q_group_box)
        self.q_progress_bar.setGeometry(240, 80, 250, 20)
        # self.q_progress_bar.setValue(0)
        self.q_progress_bar.setObjectName("q_progress_bar")

        # 添加控制台输出框
        self.q_text_edit = QtWidgets.QTextEdit(self.q_group_box)
        self.q_text_edit.setGeometry(40, 120, 500, 300)
        self.q_text_edit.setObjectName("q_text_edit")
        self.q_text_edit.setReadOnly(True)

        self.tabWidget.addTab(self.tab_1, "")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        # 设置菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.q_menu_1 = QtWidgets.QMenu(self.menubar)
        self.q_menu_1.setObjectName("q_menu_1")
        self.q_menu_2 = QtWidgets.QMenu(self.menubar)
        self.q_menu_2.setObjectName("q_menu_2")
        MainWindow.setMenuBar(self.menubar)

        # 设置状态栏
        self.q_status_bar = QtWidgets.QStatusBar(MainWindow)
        self.q_status_bar.setObjectName("q_status_bar")
        MainWindow.setStatusBar(self.q_status_bar)

        # 设置界面操作控件
        self.q_open_action = QtWidgets.QAction(MainWindow)
        self.q_open_action.setIcon(self.q_icon)
        self.q_open_action.setObjectName("q_open_action")
        self.q_exit_action = QtWidgets.QAction(MainWindow)
        self.q_exit_action.setIcon(self.q_icon)
        self.q_exit_action.setObjectName("q_exit_action")

        self.q_menu_1.addAction(self.q_open_action)
        self.q_menu_1.addSeparator()
        self.q_menu_1.addAction(self.q_exit_action)
        self.menubar.addAction(self.q_menu_1.menuAction())
        self.menubar.addAction(self.q_menu_2.menuAction())

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "数据提取工具"))
        MainWindow.setWindowTitle("数据提取工具")
        self.q_menu_1.setTitle("文件")
        self.q_open_action.setText("打开")
        self.q_open_action.setShortcut("Ctrl+O")
        self.q_exit_action.setText("退出")
        self.q_exit_action.setShortcut("Ctrl+Q")
        self.q_menu_2.setTitle("主页")

        self.q_group_box.setTitle("运行过程")
        self.q_label_1.setText("文件地址")
        self.q_label_2.setText("完成进度：")
        self.q_push_button.setText("开始")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), '数据提取')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), '数据提取2')

        # 给每个输入框添加提醒信息
        for eachLineText in [self.q_line_edit]:
            eachLineText.setToolTip("温馨提示：请确认文件是否存在！")
        # 给按钮设置鼠标变手
        for eachButton in [self.q_push_button]:
            eachButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # 设置样式
        self.myStyle()

    def myStyle(self):
        qss = Qss()
        self.setStyleSheet(qss.css)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myui = Ui_MainWindow()
    myui.show()
    sys.exit(app.exec_())
