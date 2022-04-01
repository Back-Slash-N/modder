# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(795, 526)
        icon = QIcon()
        icon.addFile(u"../../Resources/Images/MainWindowIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font: 63 14pt \"Quicksand SemiBold\";\n"
"color: rgb(104, 150, 137);\n"
"background-color: rgb(11, 60, 73);")
        self.actionGuide = QAction(MainWindow)
        self.actionGuide.setObjectName(u"actionGuide")
        self.actionCheck_for_update = QAction(MainWindow)
        self.actionCheck_for_update.setObjectName(u"actionCheck_for_update")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Button_MountMod = QPushButton(self.centralwidget)
        self.Button_MountMod.setObjectName(u"Button_MountMod")
        self.Button_MountMod.setGeometry(QRect(50, 360, 75, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 0, 100, 100))
        self.label.setPixmap(QPixmap(u"../../Resources/Images/logo.svg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 140, 81, 21))
        self.button_CopyIP = QPushButton(self.centralwidget)
        self.button_CopyIP.setObjectName(u"button_CopyIP")
        self.button_CopyIP.setGeometry(QRect(230, 130, 21, 21))
        self.button_CopyIP.setLayoutDirection(Qt.RightToLeft)
        self.button_CopyIP.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u"../../Resources/Images/copy-icon2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_CopyIP.setIcon(icon1)
        self.button_CopyIP.setCheckable(False)
        self.button_CopyIP.setFlat(True)
        self.label_PublicIP = QLabel(self.centralwidget)
        self.label_PublicIP.setObjectName(u"label_PublicIP")
        self.label_PublicIP.setGeometry(QRect(100, 130, 131, 41))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 180, 161, 31))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QRect(180, 190, 21, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 34))
        self.menuSettings_2 = QMenu(self.menubar)
        self.menuSettings_2.setObjectName(u"menuSettings_2")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings_2.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSettings_2.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionGuide)
        self.menuHelp.addAction(self.actionCheck_for_update)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Portal 2: Multiplayer Mod", None))
        self.actionGuide.setText(QCoreApplication.translate("MainWindow", u"Guide", None))
#if QT_CONFIG(statustip)
        self.actionGuide.setStatusTip(QCoreApplication.translate("MainWindow", u"opens the browser to show a guide on how to set up", None))
#endif // QT_CONFIG(statustip)
        self.actionCheck_for_update.setText(QCoreApplication.translate("MainWindow", u"Check for update", None))
#if QT_CONFIG(statustip)
        self.actionCheck_for_update.setStatusTip(QCoreApplication.translate("MainWindow", u"checks for updates for the mod", None))
#endif // QT_CONFIG(statustip)
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(statustip)
        self.actionSettings.setStatusTip(QCoreApplication.translate("MainWindow", u"opens the settings menu", None))
#endif // QT_CONFIG(statustip)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Button_MountMod.setText(QCoreApplication.translate("MainWindow", u"Mount mod", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Public IP:", None))
#if QT_CONFIG(tooltip)
        self.button_CopyIP.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.button_CopyIP.setText("")
        self.label_PublicIP.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">123.456.789.123</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#da2c38;\">Developer Mode:</span></p></body></html>", None))
        self.radioButton.setText("")
        self.menuSettings_2.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

