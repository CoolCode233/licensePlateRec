# -*- coding: utf-8 -*-

import sys, os, cv2, xlwt
import numpy as np
from sys import exit, argv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.RowLength = 0
        self.Data = [['文件名称', '录入时间', '车牌号码', '车牌类型', '车牌信息']]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1313, 670)
        MainWindow.setFixedSize(1313, 670)  # 设置窗体固定大小
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(690, 40, 511, 460))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_0.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 40, 481, 420))
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 671, 631))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 669, 629))
        self.scrollAreaWidgetContents_1.setObjectName("scrollAreaWidgetContents_1")
        self.label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_1)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_1)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 651, 581))  # 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setColumnWidth(0, 140)  # 设置1列的宽度
        self.tableWidget.setColumnWidth(1, 180)  # 设置2列的宽度
        self.tableWidget.setColumnWidth(2, 160)  # 设置3列的宽度
        self.tableWidget.setColumnWidth(3, 90)  # 设置4列的宽度
        self.tableWidget.setColumnWidth(4, 181)  # 设置5列的宽度
        self.tableWidget.setHorizontalHeaderLabels(["图片名称", "录入时间", "车牌号码", "车牌类型", "车牌信息"])
        self.tableWidget.setRowCount(self.RowLength)
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头)

        b = '''
                             color:white;
                             background:#2B2B2B;
                            '''
        # self.tableWidget.setStyleSheet(b)
        # self.tableWidget.setAlternatingRowColors(True)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.raise_()
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_1)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(690, 510, 341, 131))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 339, 129))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 321, 81))
        self.label_3.setObjectName("label_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_4.setGeometry(QtCore.QRect(1040, 510, 161, 131))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 159, 129))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 50, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.__openimage)  # 设置点击事件
        self.pushButton.setStyleSheet(
            '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#2B2B2B;}''')
        self.pushButton_2.clicked.connect(self.__writeFiles)  # 设置点击事件
        self.pushButton_2.setStyleSheet(
            '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#2B2B2B;}''')
        self.retranslateUi(MainWindow)

        self.close_widget = QtWidgets.QWidget(self.centralwidget)
        self.close_widget.setGeometry(QtCore.QRect(1130, 0, 90, 50))
        self.close_widget.setObjectName("close_widget")
        self.close_layout = QGridLayout()  # 创建左侧部件的网格布局层
        self.close_widget.setLayout(self.close_layout)  # 设置左侧部件布局为网格

        self.left_close = QPushButton("")  # 关闭按钮
        self.left_close.clicked.connect(self.close)
        self.left_visit = QPushButton("")  # 空白按钮
        self.left_visit.clicked.connect(MainWindow.big)
        self.left_mini = QPushButton("")  # 最小化按钮
        self.left_mini.clicked.connect(MainWindow.mini)
        self.close_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.close_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.close_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ProjectPath = os.getcwd()  # 获取当前工程文件位置

        self.centralwidget.setStyleSheet('''
                     QWidget#centralwidget{
                     color:white;
                     background:#222225;
                     border-top:1px solid #222225;
                     border-bottom:1px solid #222225;
                     border-right:1px solid #222225;
                     border-left:1px solid #444444;
                     border-top-left-radius:10px;
                     border-top-right-radius:10px;
                     border-bottom-left-radius:10px;
                     border-bottom-right-radius:10px;
                     }
                     ''')
        sc = '''
                     QWidget{
                     color:white;
                     background:#2B2B2B;
                     border-top:1px solid #222225;
                     border-bottom:1px solid #222225;
                     border-right:1px solid #222225;
                     border-left:1px solid #444444;
                     border-top-left-radius:10px;
                     border-top-right-radius:10px;
                     border-bottom-left-radius:10px;
                     border-bottom-right-radius:10px;
                     }

                     '''

        self.scrollAreaWidgetContents_1.setStyleSheet('''
                     QWidget{
                     color:black;
                     background:#2B2B2B;
                     border-top:1px solid #222225;
                     border-bottom:1px solid #222225;
                     border-right:1px solid #222225;
                     border-left:1px solid #444444;
                     border-top-left-radius:10px;
                     border-top-right-radius:10px;
                     border-bottom-left-radius:10px;
                     border-bottom-right-radius:10px;
                     }
                              QListWidget{background-color:#2B2B2B;color:#222225}
                 /*垂直滚动条*/
                 QScrollBar:vertical{
                     width:12px;
                     border:1px solid #2B2B2B;
                     margin:0px,0px,0px,0px;
                     padding-top:0px;
                     padding-bottom:0px;
                 }
                 QScrollBar::handle:vertical{
                     width:3px;
                     background:#4B4B4B;
                     min-height:3;
                 }
                 QScrollBar::handle:vertical:hover{
                     background:#3F3F3F;
                     border:0px #3F3F3F;
                 }
                 QScrollBar::sub-line:vertical{
                     width:0px;
                     border-image:url(:/Res/scroll_left.png);
                     subcontrol-position:left;
                 }
                 QScrollBar::sub-line:vertical:hover{
                     height:0px;
                     background:#222225;
                     subcontrol-position:top;
                 }
                 QScrollBar::add-line:vertical{
                     height:0px;
                     border-image:url(:/Res/scroll_down.png);
                     subcontrol-position:bottom;
                 }
                 QScrollBar::add-line:vertical:hover{
                     height:0px;
                     background:#3F3F3F;
                     subcontrol-position:bottom;
                 }
                 QScrollBar::add-page:vertical{
                     background:#2B2B2B;
                 }
                 QScrollBar::sub-page:vertical{
                     background:#2B2B2B;
                 }
                 QScrollBar::up-arrow:vertical{
                     border-style:outset;
                     border-width:0px;
                 }
                 QScrollBar::down-arrow:vertical{
                     border-style:outset;
                     border-width:0px;
                 }

                 QScrollBar:horizontal{
                     height:12px;
                     border:1px #2B2B2B;
                     margin:0px,0px,0px,0px;
                     padding-left:0px;
                     padding-right:0px;
                 }
                 QScrollBar::handle:horizontal{
                     height:16px;
                     background:#4B4B4B;
                     min-width:20;
                 }
                 QScrollBar::handle:horizontal:hover{
                     background:#3F3F3F;
                     border:0px #3F3F3F;
                 }
                 QScrollBar::sub-line:horizontal{
                     width:0px;
                     border-image:url(:/Res/scroll_left.png);
                     subcontrol-position:left;
                 }
                 QScrollBar::sub-line:horizontal:hover{
                     width:0px;
                     background:#2B2B2B;
                     subcontrol-position:left;
                 }
                 QScrollBar::add-line:horizontal{
                     width:0px;
                     border-image:url(:/Res/scroll_right.png);
                     subcontrol-position:right;
                 }
                 QScrollBar::add-line:horizontal:hover{
                     width:0px;
                     background::#2B2B2B;
                     subcontrol-position:right;
                 }
                 QScrollBar::add-page:horizontal{
                            background:#2B2B2B;
                 }
                 QScrollBar::sub-page:horizontal{
                             background:#2B2B2B;
                 }
                     ''')
        self.scrollAreaWidgetContents.setStyleSheet(sc)
        self.scrollAreaWidgetContents_3.setStyleSheet(sc)
        self.scrollAreaWidgetContents_4.setStyleSheet(sc)
        b = '''
                     color:white;
                     background:#2B2B2B;
                    '''
        self.label_0.setStyleSheet(b)
        self.label_1.setStyleSheet(b)
        self.label_2.setStyleSheet(b)
        self.label_3.setStyleSheet(b)

        MainWindow.setWindowOpacity(0.95)  # 设置窗口透明度
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框





# 重写MainWindow类
class MainWindow(QtWidgets.QMainWindow):

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '提示',
                                               "是否要退出程序？\n提示：退出后将丢失所有识别数据",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def mousePressEvent(self, event):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.m_flag = True
        self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
        event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
        QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.m_flag = False

    def mousePressEvent(self, event):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.m_flag = True
        self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
        event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
        QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.m_flag = False

    def big(self):
        global big
        print('最大化：{}'.format(big))
        if not big:
            self.setWindowState(Qt.WindowMaximized)
            big = True
        elif big:
            self.setWindowState(Qt.WindowNoState)
            big = False

    def mini(self):

        self.showMinimized()




if __name__ == "__main__":
    if os.path.exists('provinces.json'):
        if os.path.exists('cardtype.json'):
            if os.path.exists('Prefecture.json'):
                if os.path.exists('config.js'):
                    app = QtWidgets.QApplication(sys.argv)
                    MainWindow = MainWindow()  # QtWidgets.QMainWindow()
                    ui = Ui_MainWindow()
                    ui.setupUi(MainWindow)
                    MainWindow.show()
                    sys.exit(app.exec_())
                    # app = QApplication(argv)
                    # gui = Ui_MainWindow()
                    # gui.setupUi(MainWindow)
                    # MainWindow.show()
                    # exit(app.exec_())
                else:
                    print('未找到参数文件 config.js')
                    RuntimeError('未找到参数文件 config.js')
            else:
                print('未找到 Prefecture.json 文件')
                RuntimeError('未找到 Prefecture.json 文件')
        else:
            print('未找到 cardtype.json 文件')
            RuntimeError('未找到 cardtype.json 文件')
    else:
        print('未找到 provinces.json 文件')
        RuntimeError('未找到 provinces.json 文件')
