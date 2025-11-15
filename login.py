# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1085, 730)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background: rgba(255,255,255,0.10);\n"
"border: 1px solid rgba(255,255,255,0.32);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(342, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"#frame_2 {\n"
"	border:none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"#frame_3 {\n"
"	border: 1px solid #000000;\n"
"	border-radius: 16px;\n"
"	padding: 14px;\n"
"	background-color: rgba(255,255,255,0.64);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setStyleSheet(u"border: none;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border: none;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border: none;")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: gray;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"height: 25px;\n"
"color: #000000;\n"
"background: rgba(0,0,0,0.18);\n"
"border: 1px solid rgba(255,255,255,0.24);\n"
"border-radius: 10px;\n"
"padding: 6px 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"border: 1px solid #7c5cff;\n"
"background: rgba(0,0,0,0.12);\n"
"}\n"
"QLineEdit:disabled {\n"
"color: #9aa3b2;\n"
"background: rgba(0,0,0,0.08);\n"
"border-color: rgba(255,255,255,0.16);\n"
"}")

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setStyleSheet(u"border: none;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"height: 25px;\n"
"color: #000000;\n"
"background: rgba(0,0,0,0.18);\n"
"border: 1px solid rgba(255,255,255,0.24);\n"
"border-radius: 10px;\n"
"padding: 6px 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"border: 1px solid #7c5cff;\n"
"background: rgba(0,0,0,0.12);\n"
"}\n"
"QLineEdit:disabled {\n"
"color: #9aa3b2;\n"
"background: rgba(0,0,0,0.08);\n"
"border-color: rgba(255,255,255,0.16);\n"
"}")

        self.verticalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border: none;")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_9)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_5.addWidget(self.checkBox, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setUnderline(True)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: blue;")

        self.horizontalLayout_5.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"color: #0b1020;\n"
"font-weight: 600;\n"
"padding: 8px 14px;\n"
"border: none;\n"
"border-radius: 12px;\n"
"height: 25px;\n"
"background: qlineargradient(\n"
"x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #7c5cff,\n"
"stop:1 #00d1ff\n"
");\n"
"}\n"
"QPushButton:hover {\n"
"background: qlineargradient(\n"
"x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #8a6dff,\n"
"stop:1 #1ae0ff\n"
");\n"
"}\n"
"QPushButton:pressed {\n"
"background: qlineargradient(\n"
"x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #6c4df0,\n"
"stop:1 #00bcea\n"
");\n"
"padding-top: 9px; padding-bottom: 7px;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy3)
        self.frame_10.setStyleSheet(u"border: none;")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy3.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy3)
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setStyleSheet(u"color: gray;\n"
"border: none;")

        self.horizontalLayout_7.addWidget(self.label_7)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:blue")

        self.horizontalLayout_6.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.horizontalSpacer = QSpacerItem(342, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Welcome", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Sign in to continue", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter your account name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter password", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Remember me", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Forgot password?", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Sign in", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"No account?", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Create new account", None))
    # retranslateUi

