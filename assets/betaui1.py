# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'with menubar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnkiMaker(object):
    def setupUi(self, AnkiMaker):
        AnkiMaker.setObjectName("AnkiMaker")
        AnkiMaker.resize(544, 445)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(12)
        AnkiMaker.setFont(font)
        AnkiMaker.setStyleSheet("colour: #eaeaea")
        self.centralwidget = QtWidgets.QWidget(AnkiMaker)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.totranslate = QtWidgets.QLineEdit(self.centralwidget)
        self.totranslate.setMinimumSize(QtCore.QSize(510, 91))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(20)
        self.totranslate.setFont(font)
        self.totranslate.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-color: #bababa;\n"
"")
        self.totranslate.setText("")
        self.totranslate.setObjectName("totranslate")
        self.horizontalLayout_7.addWidget(self.totranslate)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 20)
        self.horizontalLayout_7.setStretch(2, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.newpronounce = QtWidgets.QLabel(self.centralwidget)
        self.newpronounce.setMinimumSize(QtCore.QSize(313, 30))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(14)
        self.newpronounce.setFont(font)
        self.newpronounce.setText("")
        self.newpronounce.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.newpronounce.setObjectName("newpronounce")
        self.horizontalLayout_2.addWidget(self.newpronounce)
        self.labeltranslate_2 = QtWidgets.QLabel(self.centralwidget)
        self.labeltranslate_2.setMinimumSize(QtCore.QSize(44, 30))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(14)
        self.labeltranslate_2.setFont(font)
        self.labeltranslate_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labeltranslate_2.setObjectName("labeltranslate_2")
        self.horizontalLayout_2.addWidget(self.labeltranslate_2)
        self.tags = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.tags.setFont(font)
        self.tags.setEditable(True)
        self.tags.setCurrentText("")
        self.tags.setObjectName("tags")
        self.horizontalLayout_2.addWidget(self.tags)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 50)
        self.horizontalLayout_2.setStretch(1, 600)
        self.horizontalLayout_2.setStretch(2, 240)
        self.horizontalLayout_2.setStretch(4, 47)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 9, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.hanyu = QtWidgets.QLabel(self.centralwidget)
        self.hanyu.setMinimumSize(QtCore.QSize(510, 30))
        self.hanyu.setBaseSize(QtCore.QSize(331, 0))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(14)
        self.hanyu.setFont(font)
        self.hanyu.setText("")
        self.hanyu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.hanyu.setObjectName("hanyu")
        self.horizontalLayout_5.addWidget(self.hanyu)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.horizontalLayout_5.setStretch(0, 51)
        self.horizontalLayout_5.setStretch(1, 1020)
        self.horizontalLayout_5.setStretch(2, 51)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("border-colour: #000000;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setMinimumSize(QtCore.QSize(181, 51))
        font = QtGui.QFont()
        font.setFamily("Product Sans Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"background-color: #379634;\n"
"border-radius: 10px;\n"
"border-color: #bababa;\n"
"color: white;\n"
"font-weight: normal;\n"
"")
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout_8.addWidget(self.submitButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 4)
        self.horizontalLayout_8.setStretch(2, 2)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 8, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.labeltranslate = QtWidgets.QLabel(self.centralwidget)
        self.labeltranslate.setMinimumSize(QtCore.QSize(105, 24))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(14)
        self.labeltranslate.setFont(font)
        self.labeltranslate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labeltranslate.setObjectName("labeltranslate")
        self.horizontalLayout.addWidget(self.labeltranslate)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(146, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.buffer = QtWidgets.QLabel(self.centralwidget)
        self.buffer.setMinimumSize(QtCore.QSize(242, 0))
        self.buffer.setText("")
        self.buffer.setObjectName("buffer")
        self.horizontalLayout.addWidget(self.buffer)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.horizontalLayout.setStretch(0, 20)
        self.horizontalLayout.setStretch(3, 320)
        self.horizontalLayout.setStretch(4, 5)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.translated = QtWidgets.QLineEdit(self.centralwidget)
        self.translated.setEnabled(True)
        self.translated.setMinimumSize(QtCore.QSize(510, 91))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(20)
        self.translated.setFont(font)
        self.translated.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-color: #bababa;\n"
"")
        self.translated.setText("")
        self.translated.setObjectName("translated")
        self.horizontalLayout_3.addWidget(self.translated)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 20)
        self.horizontalLayout_3.setStretch(2, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem13, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 3, 2)
        AnkiMaker.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AnkiMaker)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        AnkiMaker.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(AnkiMaker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAppearance = QtWidgets.QMenu(self.menubar)
        self.menuAppearance.setObjectName("menuAppearance")
        self.menuCard_Creation = QtWidgets.QMenu(self.menuAppearance)
        self.menuCard_Creation.setObjectName("menuCard_Creation")
        AnkiMaker.setMenuBar(self.menubar)
        self.actionDark_Mode_2 = QtWidgets.QAction(AnkiMaker)
        self.actionDark_Mode_2.setObjectName("actionDark_Mode_2")
        self.actionAppearanceChange = QtWidgets.QAction(AnkiMaker)
        self.actionAppearanceChange.setCheckable(True)
        self.actionAppearanceChange.setObjectName("actionAppearanceChange")
        self.actionMultiple = QtWidgets.QAction(AnkiMaker)
        self.actionMultiple.setObjectName("actionMultiple")
        self.actionOnly_Close_Definition = QtWidgets.QAction(AnkiMaker)
        self.actionOnly_Close_Definition.setObjectName("actionOnly_Close_Definition")
        self.actionOnly_Close_Translated = QtWidgets.QAction(AnkiMaker)
        self.actionOnly_Close_Translated.setObjectName("actionOnly_Close_Translated")
        self.actionUndo = QtWidgets.QAction(AnkiMaker)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(AnkiMaker)
        self.actionRedo.setObjectName("actionRedo")
        self.actionMultiple_2 = QtWidgets.QAction(AnkiMaker)
        self.actionMultiple_2.setCheckable(True)
        self.actionMultiple_2.setObjectName("actionMultiple_2")
        self.actionCloseDefinition = QtWidgets.QAction(AnkiMaker)
        self.actionCloseDefinition.setCheckable(True)
        self.actionCloseDefinition.setObjectName("actionCloseDefinition")
        self.actionCloseTranslated = QtWidgets.QAction(AnkiMaker)
        self.actionCloseTranslated.setCheckable(True)
        self.actionCloseTranslated.setObjectName("actionCloseTranslated")
        self.menuFile.addAction(self.actionUndo)
        self.menuFile.addAction(self.actionRedo)
        self.menuCard_Creation.addAction(self.actionMultiple_2)
        self.menuCard_Creation.addAction(self.actionCloseDefinition)
        self.menuCard_Creation.addAction(self.actionCloseTranslated)
        self.menuAppearance.addAction(self.menuCard_Creation.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAppearance.menuAction())

        self.retranslateUi(AnkiMaker)
        QtCore.QMetaObject.connectSlotsByName(AnkiMaker)

    def retranslateUi(self, AnkiMaker):
        _translate = QtCore.QCoreApplication.translate
        AnkiMaker.setWindowTitle(_translate("AnkiMaker", "MainWindow"))
        self.totranslate.setPlaceholderText(_translate("AnkiMaker", "Key in text here:"))
        self.labeltranslate_2.setText(_translate("AnkiMaker", "Tags:"))
        self.tags.setPlaceholderText(_translate("AnkiMaker", "<Enter> to save tag"))
        self.submitButton.setText(_translate("AnkiMaker", "Submit"))
        self.labeltranslate.setText(_translate("AnkiMaker", "Translate to:"))
        self.comboBox.setPlaceholderText(_translate("AnkiMaker", "choose a language!"))
        self.comboBox.setItemText(0, _translate("AnkiMaker", "English"))
        self.comboBox.setItemText(1, _translate("AnkiMaker", "Chinese (Simplified)"))
        self.comboBox.setItemText(2, _translate("AnkiMaker", "Malay"))
        self.comboBox.setItemText(3, _translate("AnkiMaker", "Hindi"))
        self.comboBox.setItemText(4, _translate("AnkiMaker", "Tamil"))
        self.comboBox.setItemText(5, _translate("AnkiMaker", "Filipino"))
        self.comboBox.setItemText(6, _translate("AnkiMaker", "Japanese"))
        self.comboBox.setItemText(7, _translate("AnkiMaker", "Vietnamese"))
        self.comboBox.setItemText(8, _translate("AnkiMaker", "Spanish"))
        self.comboBox.setItemText(9, _translate("AnkiMaker", "Arabic"))
        self.comboBox.setItemText(10, _translate("AnkiMaker", "Chinese (Traditional)"))
        self.comboBox.setItemText(11, _translate("AnkiMaker", "French"))
        self.comboBox.setItemText(12, _translate("AnkiMaker", "German"))
        self.comboBox.setItemText(13, _translate("AnkiMaker", "Greek"))
        self.comboBox.setItemText(14, _translate("AnkiMaker", "Indonesian"))
        self.comboBox.setItemText(15, _translate("AnkiMaker", "Italian"))
        self.comboBox.setItemText(16, _translate("AnkiMaker", "Javanese"))
        self.comboBox.setItemText(17, _translate("AnkiMaker", "Korean"))
        self.comboBox.setItemText(18, _translate("AnkiMaker", "Latin"))
        self.comboBox.setItemText(19, _translate("AnkiMaker", "Myanmar (Burmese)"))
        self.comboBox.setItemText(20, _translate("AnkiMaker", "Polish"))
        self.comboBox.setItemText(21, _translate("AnkiMaker", "Portugese"))
        self.comboBox.setItemText(22, _translate("AnkiMaker", "Russian"))
        self.comboBox.setItemText(23, _translate("AnkiMaker", "Thai"))
        self.comboBox.setItemText(24, _translate("AnkiMaker", "Ukrainian"))
        self.comboBox.setItemText(25, _translate("AnkiMaker", "Yiddish"))
        self.translated.setPlaceholderText(_translate("AnkiMaker", "Amend translated text here:"))
        self.menuFile.setTitle(_translate("AnkiMaker", "File"))
        self.menuAppearance.setTitle(_translate("AnkiMaker", "Edit"))
        self.menuCard_Creation.setTitle(_translate("AnkiMaker", "Card Creation"))
        self.actionDark_Mode_2.setText(_translate("AnkiMaker", "Dark Mode"))
        self.actionAppearanceChange.setText(_translate("AnkiMaker", "Dark Mode"))
        self.actionMultiple.setText(_translate("AnkiMaker", "Multiple"))
        self.actionOnly_Close_Definition.setText(_translate("AnkiMaker", "Only Close Definition"))
        self.actionOnly_Close_Translated.setText(_translate("AnkiMaker", "Only Close Translated"))
        self.actionUndo.setText(_translate("AnkiMaker", "Undo Submit"))
        self.actionUndo.setShortcut(_translate("AnkiMaker", "Ctrl+Shift+Z"))
        self.actionRedo.setText(_translate("AnkiMaker", "Redo Submit"))
        self.actionRedo.setShortcut(_translate("AnkiMaker", "Ctrl+Shift+Y"))
        self.actionMultiple_2.setText(_translate("AnkiMaker", "Multiple"))
        self.actionCloseDefinition.setText(_translate("AnkiMaker", "Only Close Definition"))
        self.actionCloseTranslated.setText(_translate("AnkiMaker", "Only Close Translated"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnkiMaker = QtWidgets.QMainWindow()
    ui = Ui_AnkiMaker()
    ui.setupUi(AnkiMaker)
    AnkiMaker.show()
    sys.exit(app.exec_())