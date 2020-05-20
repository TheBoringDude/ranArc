# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ranarc.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"app.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnFindArticle = QPushButton(self.centralwidget)
        self.btnFindArticle.setObjectName(u"btnFindArticle")
        self.btnFindArticle.setGeometry(QRect(80, 120, 241, 51))
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(15)
        self.btnFindArticle.setFont(font)
        self.btnFindArticle.setStyleSheet(u"background-color: rgb(0, 118, 214);\n"
"color: rgb(255, 255, 255);")
        self.btnFindArticle.setAutoDefault(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 9, 381, 61))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Black")
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(221, 79, 66);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 59, 361, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btnFindArticle.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RanARC", None))
        self.btnFindArticle.setText(QCoreApplication.translate("MainWindow", u"FIND", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RanARC", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Internet Random Article Finder", None))
    # retranslateUi

