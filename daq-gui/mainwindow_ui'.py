# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_sample_rate = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_sample_rate.sizePolicy().hasHeightForWidth())
        self.lineEdit_sample_rate.setSizePolicy(sizePolicy)
        self.lineEdit_sample_rate.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_sample_rate.setMaxLength(5)
        self.lineEdit_sample_rate.setFrame(True)
        self.lineEdit_sample_rate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_sample_rate.setObjectName(_fromUtf8("lineEdit_sample_rate"))
        self.horizontalLayout.addWidget(self.lineEdit_sample_rate)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        #single ended tab
        self.tab_single = QtGui.QWidget()
        self.tab_single.setObjectName(_fromUtf8("tab_single"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_single)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_single)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        self.label_k = QtGui.QLabel()    #added thing
        self.label_k.setText("K")
        self.label_k.setStyleSheet('color: black')   #added thing
        self.checkBox_chan5 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_chan5.setObjectName(_fromUtf8("checkBox_chan5"))
        self.gridLayout_2.addWidget(self.checkBox_chan5, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.label_k, 2,3,1,1)   #added thing
        
        self.label_r = QtGui.QLabel()    #added thing
        self.label_r.setText("R")
        self.label_r.setStyleSheet('color: red')   #added thing
        self.checkBox_chan0 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_chan0.setChecked(True)
        self.checkBox_chan0.setObjectName(_fromUtf8("checkBox_chan0"))
        self.gridLayout_2.addWidget(self.checkBox_chan0, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_r, 0,1,1,1)   #added thing
        
        self.checkBox_chan1 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_chan1.setObjectName(_fromUtf8("checkBox_chan1"))
        self.gridLayout_2.addWidget(self.checkBox_chan1, 0, 2, 1, 1)
        

        self.checkBox_chan3 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_chan3.setObjectName(_fromUtf8("checkBox_chan3"))
        self.gridLayout_2.addWidget(self.checkBox_chan3, 1, 1, 1, 1)
        

        self.checkBox_chan4 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_chan4.setObjectName(_fromUtf8("checkBox_chan4"))
        self.gridLayout_2.addWidget(self.checkBox_chan4, 2, 0, 1, 1)
        

        self.checkBox_chan2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_chan2.setObjectName(_fromUtf8("checkBox_chan2"))
        self.gridLayout_2.addWidget(self.checkBox_chan2, 1, 0, 1, 1)
        

        self.checkBox_chan6 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_chan6.setObjectName(_fromUtf8("checkBox_chan6"))
        self.gridLayout_2.addWidget(self.checkBox_chan6, 3, 0, 1, 1)
        

        self.checkBox_chan7 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_chan7.setObjectName(_fromUtf8("checkBox_chan7"))
        self.gridLayout_2.addWidget(self.checkBox_chan7, 3, 1, 1, 1)
        
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_single, _fromUtf8(""))
        
        #differential tab
        self.tab_diff = QtGui.QWidget()
        self.tab_diff.setObjectName(_fromUtf8("tab_diff"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_diff)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_diff)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkBox_chan32 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_chan32.setObjectName(_fromUtf8("checkBox_chan32"))
        self.gridLayout_3.addWidget(self.checkBox_chan32, 3, 0, 1, 1)
        self.checkBox_chan76 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_chan76.setObjectName(_fromUtf8("checkBox_chan76"))
        self.gridLayout_3.addWidget(self.checkBox_chan76, 5, 0, 1, 1)
        self.checkBox_chan54 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_chan54.setObjectName(_fromUtf8("checkBox_chan54"))
        self.gridLayout_3.addWidget(self.checkBox_chan54, 4, 0, 1, 1)
        self.checkBox_chan10 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_chan10.setChecked(True)
        self.checkBox_chan10.setObjectName(_fromUtf8("checkBox_chan10"))
        self.gridLayout_3.addWidget(self.checkBox_chan10, 0, 0, 1, 1)
        
        #comboboxes
        self.comboBox_gain_1 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_gain_1.setObjectName(_fromUtf8("comboBox_gain_1"))
        self.comboBox_gain_1.addItem(_fromUtf8(""))
        self.comboBox_gain_1.addItem(_fromUtf8(""))
        self.comboBox_gain_1.addItem(_fromUtf8(""))
        self.comboBox_gain_1.addItem(_fromUtf8(""))
        self.comboBox_gain_1.addItem(_fromUtf8(""))
        self.comboBox_gain_1.addItem(_fromUtf8(""))
        self.comboBox_gain_1.addItem(_fromUtf8(""))
        self.comboBox_gain_1.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_gain_1, 0, 1, 1, 1)
        self.comboBox_gain_2 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_gain_2.setObjectName(_fromUtf8("comboBox_gain_2"))
        self.comboBox_gain_2.addItem(_fromUtf8(""))
        self.comboBox_gain_2.addItem(_fromUtf8(""))
        self.comboBox_gain_2.addItem(_fromUtf8(""))
        self.comboBox_gain_2.addItem(_fromUtf8(""))
        self.comboBox_gain_2.addItem(_fromUtf8(""))
        self.comboBox_gain_2.addItem(_fromUtf8(""))
        self.comboBox_gain_2.addItem(_fromUtf8(""))
        self.comboBox_gain_2.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_gain_2, 3, 1, 1, 1)
        self.comboBox_gain_3 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_gain_3.setObjectName(_fromUtf8("comboBox_gain_3"))
        self.comboBox_gain_3.addItem(_fromUtf8(""))
        self.comboBox_gain_3.addItem(_fromUtf8(""))
        self.comboBox_gain_3.addItem(_fromUtf8(""))
        self.comboBox_gain_3.addItem(_fromUtf8(""))
        self.comboBox_gain_3.addItem(_fromUtf8(""))
        self.comboBox_gain_3.addItem(_fromUtf8(""))
        self.comboBox_gain_3.addItem(_fromUtf8(""))
        self.comboBox_gain_3.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_gain_3, 4, 1, 1, 1)
        self.comboBox_gain_4 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_gain_4.setObjectName(_fromUtf8("comboBox_gain_4"))
        self.comboBox_gain_4.addItem(_fromUtf8(""))
        self.comboBox_gain_4.addItem(_fromUtf8(""))
        self.comboBox_gain_4.addItem(_fromUtf8(""))
        self.comboBox_gain_4.addItem(_fromUtf8(""))
        self.comboBox_gain_4.addItem(_fromUtf8(""))
        self.comboBox_gain_4.addItem(_fromUtf8(""))
        self.comboBox_gain_4.addItem(_fromUtf8(""))
        self.comboBox_gain_4.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_gain_4, 5, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab_diff, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_tmin = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tmin.sizePolicy().hasHeightForWidth())
        self.lineEdit_tmin.setSizePolicy(sizePolicy)
        self.lineEdit_tmin.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_tmin.setMaxLength(5)
        self.lineEdit_tmin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_tmin.setObjectName(_fromUtf8("lineEdit_tmin"))
        self.horizontalLayout_2.addWidget(self.lineEdit_tmin)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_tmax = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tmax.sizePolicy().hasHeightForWidth())
        self.lineEdit_tmax.setSizePolicy(sizePolicy)
        self.lineEdit_tmax.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_tmax.setMaxLength(5)
        self.lineEdit_tmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_tmax.setObjectName(_fromUtf8("lineEdit_tmax"))
        self.horizontalLayout_2.addWidget(self.lineEdit_tmax)
        self.comboBox_time = QtGui.QComboBox(self.centralwidget)
        self.comboBox_time.setObjectName(_fromUtf8("comboBox_time"))
        self.comboBox_time.addItem(_fromUtf8(""))
        self.comboBox_time.addItem(_fromUtf8(""))
        self.comboBox_time.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_time)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_ymin = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ymin.sizePolicy().hasHeightForWidth())
        self.lineEdit_ymin.setSizePolicy(sizePolicy)
        self.lineEdit_ymin.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_ymin.setMaxLength(5)
        self.lineEdit_ymin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ymin.setObjectName(_fromUtf8("lineEdit_ymin"))
        self.horizontalLayout_3.addWidget(self.lineEdit_ymin)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_ymax = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ymax.sizePolicy().hasHeightForWidth())
        self.lineEdit_ymax.setSizePolicy(sizePolicy)
        self.lineEdit_ymax.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_ymax.setMaxLength(5)
        self.lineEdit_ymax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ymax.setObjectName(_fromUtf8("lineEdit_ymax"))
        self.horizontalLayout_3.addWidget(self.lineEdit_ymax)
        self.comboBox_y = QtGui.QComboBox(self.centralwidget)
        self.comboBox_y.setObjectName(_fromUtf8("comboBox_y"))
        self.comboBox_y.addItem(_fromUtf8(""))
        self.comboBox_y.addItem(_fromUtf8(""))
        self.comboBox_y.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboBox_y)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_start = QtGui.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.horizontalLayout_4.addWidget(self.pushButton_start)
        self.pushButton_stop = QtGui.QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.horizontalLayout_4.addWidget(self.pushButton_stop)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 2, 1)
        self.label_title = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setLineWidth(1)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.gridLayout.addWidget(self.label_title, 0, 1, 1, 1)
        self.plotWidget = PlotWidget(self.centralwidget)
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.gridLayout.addWidget(self.plotWidget, 1, 1, 3, 1)
        self.checkBox_roi = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_roi.setObjectName(_fromUtf8("checkBox_roi"))
        self.gridLayout.addWidget(self.checkBox_roi, 4, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 0, 2, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.plotWidget.raise_()
        self.label_title.raise_()
        self.checkBox_roi.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_sample_rate, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.checkBox_chan0)
        MainWindow.setTabOrder(self.checkBox_chan0, self.checkBox_chan1)
        MainWindow.setTabOrder(self.checkBox_chan1, self.checkBox_chan2)
        MainWindow.setTabOrder(self.checkBox_chan2, self.checkBox_chan3)
        MainWindow.setTabOrder(self.checkBox_chan3, self.checkBox_chan4)
        MainWindow.setTabOrder(self.checkBox_chan4, self.checkBox_chan5)
        MainWindow.setTabOrder(self.checkBox_chan5, self.checkBox_chan6)
        MainWindow.setTabOrder(self.checkBox_chan6, self.checkBox_chan7)
        MainWindow.setTabOrder(self.checkBox_chan7, self.checkBox_chan10)
        MainWindow.setTabOrder(self.checkBox_chan10, self.comboBox_gain_1)
        MainWindow.setTabOrder(self.comboBox_gain_1, self.checkBox_chan32)
        MainWindow.setTabOrder(self.checkBox_chan32, self.comboBox_gain_2)
        MainWindow.setTabOrder(self.comboBox_gain_2, self.checkBox_chan54)
        MainWindow.setTabOrder(self.checkBox_chan54, self.comboBox_gain_3)
        MainWindow.setTabOrder(self.comboBox_gain_3, self.checkBox_chan76)
        MainWindow.setTabOrder(self.checkBox_chan76, self.comboBox_gain_4)
        MainWindow.setTabOrder(self.comboBox_gain_4, self.lineEdit_tmin)
        MainWindow.setTabOrder(self.lineEdit_tmin, self.lineEdit_tmax)
        MainWindow.setTabOrder(self.lineEdit_tmax, self.comboBox_time)
        MainWindow.setTabOrder(self.comboBox_time, self.lineEdit_ymin)
        MainWindow.setTabOrder(self.lineEdit_ymin, self.lineEdit_ymax)
        MainWindow.setTabOrder(self.lineEdit_ymax, self.comboBox_y)
        MainWindow.setTabOrder(self.comboBox_y, self.pushButton_start)
        MainWindow.setTabOrder(self.pushButton_start, self.pushButton_stop)
        MainWindow.setTabOrder(self.pushButton_stop, self.plotWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MCC DAQ Monitor", None))
        self.label.setText(_translate("MainWindow", "Sample rate :", None))
        self.label_2.setText(_translate("MainWindow", "ms", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Select ADC Channel(s): 0 - 10V", None))
        self.checkBox_chan5.setText(_translate("MainWindow", "A5 (Pin 8)", None))
        self.checkBox_chan0.setText(_translate("MainWindow", "A0 (Pin 1)", None))
        self.checkBox_chan1.setText(_translate("MainWindow", "A1 (Pin 2)", None))
        self.checkBox_chan3.setText(_translate("MainWindow", "A3 (Pin 5)", None))
        self.checkBox_chan4.setText(_translate("MainWindow", "A4 (Pin 7)", None))
        self.checkBox_chan2.setText(_translate("MainWindow", "A2 (Pin 4)", None))
        self.checkBox_chan6.setText(_translate("MainWindow", "A6 (Pin 10)", None))
        self.checkBox_chan7.setText(_translate("MainWindow", "A7 (Pin 11)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_single), _translate("MainWindow", "Single Ended", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Select ADC Channel-Gain Pair(s):", None))
        self.checkBox_chan32.setText(_translate("MainWindow", "A2 - A3", None))
        self.checkBox_chan76.setText(_translate("MainWindow", "A6 - A7", None))
        self.checkBox_chan54.setText(_translate("MainWindow", "A4 - A5", None))
        self.checkBox_chan10.setText(_translate("MainWindow", "A0 - A1", None))
        self.comboBox_gain_1.setItemText(0, _translate("MainWindow", "+/-20V", None))
        self.comboBox_gain_1.setItemText(1, _translate("MainWindow", "+/-10V", None))
        self.comboBox_gain_1.setItemText(2, _translate("MainWindow", "+/-5V", None))
        self.comboBox_gain_1.setItemText(3, _translate("MainWindow", "+/-4V", None))
        self.comboBox_gain_1.setItemText(4, _translate("MainWindow", "+/-2.5V", None))
        self.comboBox_gain_1.setItemText(5, _translate("MainWindow", "+/-2V", None))
        self.comboBox_gain_1.setItemText(6, _translate("MainWindow", "+/-1.25V", None))
        self.comboBox_gain_1.setItemText(7, _translate("MainWindow", "+/-1V", None))
        self.comboBox_gain_2.setItemText(0, _translate("MainWindow", "+/-20V", None))
        self.comboBox_gain_2.setItemText(1, _translate("MainWindow", "+/-10V", None))
        self.comboBox_gain_2.setItemText(2, _translate("MainWindow", "+/-5V", None))
        self.comboBox_gain_2.setItemText(3, _translate("MainWindow", "+/-4V", None))
        self.comboBox_gain_2.setItemText(4, _translate("MainWindow", "+/-2.5V", None))
        self.comboBox_gain_2.setItemText(5, _translate("MainWindow", "+/-2V", None))
        self.comboBox_gain_2.setItemText(6, _translate("MainWindow", "+/-1.25V", None))
        self.comboBox_gain_2.setItemText(7, _translate("MainWindow", "+/-1V", None))
        self.comboBox_gain_3.setItemText(0, _translate("MainWindow", "+/-20V", None))
        self.comboBox_gain_3.setItemText(1, _translate("MainWindow", "+/-10V", None))
        self.comboBox_gain_3.setItemText(2, _translate("MainWindow", "+/-5V", None))
        self.comboBox_gain_3.setItemText(3, _translate("MainWindow", "+/-4V", None))
        self.comboBox_gain_3.setItemText(4, _translate("MainWindow", "+/-2.5V", None))
        self.comboBox_gain_3.setItemText(5, _translate("MainWindow", "+/-2V", None))
        self.comboBox_gain_3.setItemText(6, _translate("MainWindow", "+/-1.25V", None))
        self.comboBox_gain_3.setItemText(7, _translate("MainWindow", "+/-1V", None))
        self.comboBox_gain_4.setItemText(0, _translate("MainWindow", "+/-20V", None))
        self.comboBox_gain_4.setItemText(1, _translate("MainWindow", "+/-10V", None))
        self.comboBox_gain_4.setItemText(2, _translate("MainWindow", "+/-5V", None))
        self.comboBox_gain_4.setItemText(3, _translate("MainWindow", "+/-4V", None))
        self.comboBox_gain_4.setItemText(4, _translate("MainWindow", "+/-2.5V", None))
        self.comboBox_gain_4.setItemText(5, _translate("MainWindow", "+/-2V", None))
        self.comboBox_gain_4.setItemText(6, _translate("MainWindow", "+/-1.25V", None))
        self.comboBox_gain_4.setItemText(7, _translate("MainWindow", "+/-1V", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_diff), _translate("MainWindow", "Differential", None))
        self.label_7.setText(_translate("MainWindow", "Plot interval:", None))
        self.label_3.setText(_translate("MainWindow", "X:", None))
        self.label_4.setText(_translate("MainWindow", "to", None))
        self.comboBox_time.setItemText(0, _translate("MainWindow", "s", None))
        self.comboBox_time.setItemText(1, _translate("MainWindow", "ms", None))
        self.comboBox_time.setItemText(2, _translate("MainWindow", "us", None))
        self.label_5.setText(_translate("MainWindow", "Y:", None))
        self.label_6.setText(_translate("MainWindow", "to", None))
        self.comboBox_y.setItemText(0, _translate("MainWindow", "V", None))
        self.comboBox_y.setItemText(1, _translate("MainWindow", "mV", None))
        self.comboBox_y.setItemText(2, _translate("MainWindow", "uV", None))
        self.pushButton_start.setText(_translate("MainWindow", "Start", None))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop", None))
        self.label_title.setText(_translate("MainWindow", "Plot Title", None))
        self.checkBox_roi.setText(_translate("MainWindow", "Enable Region of Interest (ROI)", None))

from pyqtgraph import PlotWidget