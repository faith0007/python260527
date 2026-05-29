# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Chap10_ProductList.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(559, 642)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 91, 31))
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 101, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 140, 101, 31))
        self.label_3.setFont(font)
        self.prodID = QLineEdit(self.centralwidget)
        self.prodID.setObjectName(u"prodID")
        self.prodID.setGeometry(QRect(160, 40, 71, 31))
        self.prodName = QLineEdit(self.centralwidget)
        self.prodName.setObjectName(u"prodName")
        self.prodName.setGeometry(QRect(160, 90, 111, 31))
        self.prodPrice = QLineEdit(self.centralwidget)
        self.prodPrice.setObjectName(u"prodPrice")
        self.prodPrice.setGeometry(QRect(160, 140, 111, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 40, 121, 41))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(310, 90, 121, 41))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(310, 140, 121, 41))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(310, 190, 121, 41))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 250, 421, 311))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 559, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.addProduct)
        self.pushButton_2.clicked.connect(MainWindow.updateProduct)
        self.pushButton_4.clicked.connect(MainWindow.getProduct)
        self.pushButton_3.clicked.connect(MainWindow.removeProduct)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc81c\ud488ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc81c\ud488\uc774\ub984:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc81c\ud488\uac00\uaca9:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
    # retranslateUi

