from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        print(directory1)

        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          "./",
                                                          "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, filetype)

        files, ok1 = QFileDialog.getOpenFileNames(self,
                                                  "多文件选择",
                                                  "./",
                                                  "All Files (*);;Text Files (*.txt)")
        print(files, ok1)

        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "./",
                                                     "All Files (*);;Text Files (*.txt)")


if __name__ == "__main__":
    import sys
    import time, datetime
    import re
    import os

    print(time.time())
    curDate = datetime.datetime.now()
    print(curDate, type(curDate))
    print(curDate.strftime("%Y-%m-%d"))
    walk = os.walk("C:/Users/Administrator/Desktop/python")
    print(walk, type(walk))
    for rootDir, t1, fileNames in walk:
        print(rootDir)
        for fileName in fileNames:
            scriptPath = os.path.join(rootDir, fileName)
            # print(scriptPath)

    ourFileName = "res_" + curDate.strftime("%Y%m%d%H%M%S") + ".csv"
    with open(ourFileName, 'w') as f:
        f.write('TARGET_TABL,SOURCE_TABLE\n')
    with open(ourFileName, 'a') as f:
        f.write("呵呵")
        print("")

    path = "C:/Users/Administrator/Desktop/python/DWD_INSR_PLY_BASE_INFO_DF_1.hql"
    res = set()
    with open(path, 'r', encoding="UTF-8") as f:
        lines = ''.join(f.readlines()).replace("\n", "").upper()
        # searchObj = re.search(r'(FROM|JOIN)[\s]+[\S]+', lines, re.M | re.I)
        # 分两次正则，尬尬
        # findall = re.findall(r'(FROM|JOIN)[\s]+([\S]+)', lines)
        fromAll = re.findall(r'FROM[\s]+([\S]+)', lines)
        joinAll = re.findall(r'JOIN[\s]+([\S]+)', lines)
        findall = fromAll + joinAll
        for tableName in findall:
            tableName = re.sub("\${[\S]+}\.", "", tableName)
            res.add(tableName)
        print(",".join(res))

    with open(path, 'r', encoding="UTF-8") as f:
        lines = f.readlines()
        lines = "".join(lines)
        # print(lines.replace("\r\n", ""))
        searchObj = re.search(r'(FROM|JOIN)[\s]+[\S]+', lines, re.M | re.I)
        if searchObj:
            print("searchObj.group() : ", searchObj.group())
            print("searchObj.group(1) : ", searchObj.group(1))
            print("searchObj.group(2) : ", searchObj.group(2))
        else:
            print("Nothing found!!")
# app = QtWidgets.QApplication(sys.argv)
# myshow = MyWindow()
# myshow.show()
# sys.exit(app.exec_())
