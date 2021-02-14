from ui.tool_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import time, datetime
from api.tool_api import DataProcess
import traceback


class MainUI(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # 打开操作菜单栏 connect 到打开系统文件夹
        self.q_open_action.triggered.connect(QtWidgets.QFileDialog.getOpenFileName)
        # self.q_open_action.triggered.connect(self.msg)
        # 退出操作菜单栏 connect 到窗口的close方法
        self.q_exit_action.triggered.connect(self.close)
        self.q_push_button.clicked.connect(self.startThread)

    def msg(self):
        # directory1 = QtWidgets.QFileDialog.getExistingDirectory(self,
        #                                                         "选取文件夹",
        #                                                         "./")  # 起始路径
        # print(directory1)

        fileName1, filetype = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                    "选取文件",
                                                                    "./",
                                                                    "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, filetype)
        self.q_line_edit.setText(fileName1)

        # files, ok1 = QtWidgets.QFileDialog.getOpenFileNames(self,
        #                                                     "多文件选择",
        #                                                     "./",
        #                                                     "All Files (*);;Text Files (*.txt)")
        # print(files, ok1)
        #
        # fileName2, ok2 = QtWidgets.QFileDialog.getSaveFileName(self,
        #                                                        "文件保存",
        #                                                        "./",
        #                                                        "All Files (*);;Text Files (*.txt)")

    def closeEvent(self, event: QtGui.QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self, "关闭程序", "关闭程序可能导致正在运行的操作终止" \
                                                             "，请确认\n\n是否退出并关闭程序"
                                               , QtWidgets.QMessageBox.Yes
                                               , QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 启动处理线程
    def startThread(self):
        self.q_status_bar.setStyleSheet("color:green")
        self.q_push_button.setDisabled(True)
        self.q_text_edit.setText("")

        lineStr = self.q_line_edit.text()
        self.process_thread = DataProcessThread(lineStr)
        print("输入目录：", lineStr)

        self.process_thread.status_signal.connect(self.statuShow)
        self.process_thread.text_signal.connect(self.textShow)
        self.process_thread.pro_bar_max_signal.connect(self.setProgressBarVal)
        self.process_thread.pro_bar_signal.connect(self.progressBarUpdateVal)
        self.process_thread.finished.connect(self.buttonOn)
        self.process_thread.start()

    def textShow(self, str):
        self.q_text_edit.append(str)

    # 设置按钮可用
    def buttonOn(self):
        self.q_push_button.setDisabled(False)

    # 状态栏显示信息
    def statuShow(self, str):
        self.q_status_bar.showMessage(str)

    def setProgressBarVal(self, n):
        self.q_progress_bar.setMinimum(0)
        self.q_progress_bar.setMaximum(n)

    def progressBarUpdateVal(self, n):
        self.q_progress_bar.setValue(n)


class DataProcessThread(QtCore.QThread):
    status_signal = QtCore.pyqtSignal(str)  # 定义状态栏的信号
    text_signal = QtCore.pyqtSignal(str)  # 定义输出框的信号
    pro_bar_max_signal = QtCore.pyqtSignal(int)  # 进度条的信号量
    pro_bar_signal = QtCore.pyqtSignal(int)  # 进度条的信号量

    def __init__(self, tName):
        super().__init__()
        self.tName = tName
        self.api = DataProcess()

    def run(self):
        startTime = time.time()
        curDate = datetime.datetime.now()
        print(startTime)
        self.status_signal.emit("当前状态：正在进行数据提取操作。。。")
        # --------------
        #  # 测试
        # time.sleep(2)
        # self.text_signal.emit("正在读取dwd_ply_base_info_df.hql")
        # time.sleep(1)
        # self.text_signal.emit("读取dwd_ply_base_info_df.hql完成")
        # --------------
        try:
            scriptPaths = self.api.getHqlScriptPaths(self.tName)
            # --------------
            # # 测试
            # s = 1 / 0
            # --------------
        except Exception as e:
            self.text_signal.emit(self.api.getFmtMsg(msg="读取文件失败了!", color="red"))
        else:
            print(scriptPaths)
            scriptSize = len(scriptPaths)
            self.pro_bar_max_signal.emit(scriptSize)
            ourFile = "res_" + curDate.strftime("%Y%m%d%H%M%S") + ".csv";
            self.text_signal.emit(self.api.getFmtMsg("black", "文件共计{}个,开始分析依赖。".format(scriptSize)))
            with open(ourFile, 'w') as f:
                f.write('TARGET_TABL,SOURCE_TABLE\n')
            i = 1
            for scriptPath in scriptPaths:
                try:
                    self.api.sciptAnalysis(scriptPath, ourFile)
                except Exception as e:
                    traceback.print_exc()
                    msg = "文件共计{}个，解析第{}个失败，文件名：{}。".format(scriptSize, i, scriptPath)
                    self.text_signal.emit(self.api.getFmtMsg("red", msg))
                else:
                    msg = "文件共计{}个，解析第{}个。".format(scriptSize, i)
                    self.text_signal.emit(self.api.getFmtMsg("green", msg))
                self.pro_bar_signal.emit(i)
                i += 1
                time.sleep(1)
        endTime = time.time()
        print(endTime)
        msg = "当前文件读取完毕，耗时：%0.2f秒！" % (float(endTime - startTime))
        self.text_signal.emit(msg)
        self.status_signal.emit("数据处理完成!")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    sys.exit(app.exec_())
