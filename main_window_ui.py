# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(695, 572)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 58))
        font = QFont()
        font.setFamily(u"Umpush")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color:rgb(150,150,150);\n"
"color:white")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 27))
        font1 = QFont()
        font1.setFamily(u"Ubuntu Condensed")
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:rgb(200,200,200)")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.function_input = QLineEdit(self.layoutWidget)
        self.function_input.setObjectName(u"function_input")
        self.function_input.setMaximumSize(QSize(16777215, 27))
        font2 = QFont()
        font2.setPointSize(12)
        self.function_input.setFont(font2)

        self.verticalLayout_4.addWidget(self.function_input)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 27))
        font3 = QFont()
        font3.setFamily(u"Ubuntu Condensed")
        font3.setPointSize(14)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background-color:rgb(200,200,200)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.min_value_input = QLineEdit(self.layoutWidget)
        self.min_value_input.setObjectName(u"min_value_input")
        self.min_value_input.setMaximumSize(QSize(100, 27))
        self.min_value_input.setFont(font2)

        self.verticalLayout_2.addWidget(self.min_value_input)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 27))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color:rgb(200,200,200)")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.max_value_input = QLineEdit(self.layoutWidget)
        self.max_value_input.setObjectName(u"max_value_input")
        self.max_value_input.setMaximumSize(QSize(100, 27))
        self.max_value_input.setFont(font2)

        self.verticalLayout_5.addWidget(self.max_value_input)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 28))
        self.pushButton.setFont(font1)

        self.verticalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 28))
        font4 = QFont()
        font4.setPointSize(13)
        self.pushButton_2.setFont(font4)

        self.verticalLayout_7.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.splitter.addWidget(self.layoutWidget)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.Plotting_Layout = QVBoxLayout(self.verticalLayoutWidget)
        self.Plotting_Layout.setObjectName(u"Plotting_Layout")
        self.Plotting_Layout.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.verticalLayoutWidget)

        self.horizontalLayout_4.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 695, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Function Plotter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Function Plotter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Function of x:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Min Value:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Max Value:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save Figure", None))
    # retranslateUi

