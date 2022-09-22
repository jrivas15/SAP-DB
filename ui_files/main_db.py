# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_db.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(375, 231)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(33)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.ip_line = QLineEdit(self.frame)
        self.ip_line.setObjectName(u"ip_line")
        self.ip_line.setMinimumSize(QSize(50, 0))
        self.ip_line.setMaximumSize(QSize(299, 16777215))

        self.horizontalLayout_2.addWidget(self.ip_line)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setMinimumSize(QSize(17, 27))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_crear = QPushButton(self.frame)
        self.btn_crear.setObjectName(u"btn_crear")
        self.btn_crear.setMinimumSize(QSize(47, 53))
        self.btn_crear.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setPointSize(22)
        self.btn_crear.setFont(font1)
        self.btn_crear.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(85,98,112,255);\n"
"	color:rgba(255,255,255,200);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(255,107,107,255);\n"
"	color:rgba(255,255,255,200);\n"
"	background-position:calc(100% - 10px)center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgba(255,107,107,255);\n"
"}\n"
"\n"
"")
        self.btn_crear.setIconSize(QSize(36, 36))

        self.horizontalLayout.addWidget(self.btn_crear)

        self.btn_cerrar = QPushButton(self.frame)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setMinimumSize(QSize(47, 53))
        self.btn_cerrar.setMaximumSize(QSize(150, 16777215))
        self.btn_cerrar.setFont(font1)
        self.btn_cerrar.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(85,98,112,255);\n"
"	color:rgba(255,255,255,200);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(255,107,107,255);\n"
"	color:rgba(255,255,255,200);\n"
"	background-position:calc(100% - 10px)center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgba(255,107,107,255);\n"
"}\n"
"\n"
"")
        self.btn_cerrar.setIconSize(QSize(36, 36))

        self.horizontalLayout.addWidget(self.btn_cerrar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Crear DB-SAP", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"IP", None))
        self.btn_crear.setText(QCoreApplication.translate("Form", u"Crear", None))
        self.btn_cerrar.setText(QCoreApplication.translate("Form", u"Salir", None))
    # retranslateUi

