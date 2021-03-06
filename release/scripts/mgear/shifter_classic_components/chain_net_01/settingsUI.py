import mgear.core.pyqt as gqt
QtGui, QtCore, QtWidgets, wrapInstance = gqt.qt_import()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(429, 622)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.overrideJntNb_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.overrideJntNb_checkBox.setText("Override Joints Number")
        self.overrideJntNb_checkBox.setObjectName("overrideJntNb_checkBox")
        self.gridLayout_3.addWidget(self.overrideJntNb_checkBox, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.jntNb_label = QtWidgets.QLabel(self.groupBox_2)
        self.jntNb_label.setObjectName("jntNb_label")
        self.horizontalLayout.addWidget(self.jntNb_label)
        self.jntNb_spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.jntNb_spinBox.setMinimum(1)
        self.jntNb_spinBox.setProperty("value", 3)
        self.jntNb_spinBox.setObjectName("jntNb_spinBox")
        self.horizontalLayout.addWidget(self.jntNb_spinBox)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.masterB_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.masterB_lineEdit.setObjectName("masterB_lineEdit")
        self.horizontalLayout_4.addWidget(self.masterB_lineEdit)
        self.masterB_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.masterB_pushButton.setObjectName("masterB_pushButton")
        self.horizontalLayout_4.addWidget(self.masterB_pushButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.masterA_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.masterA_lineEdit.setObjectName("masterA_lineEdit")
        self.horizontalLayout_2.addWidget(self.masterA_lineEdit)
        self.masterA_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.masterA_pushButton.setObjectName("masterA_pushButton")
        self.horizontalLayout_2.addWidget(self.masterA_pushButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.jntNb_label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.jntNb_label_2.setObjectName("jntNb_label_2")
        self.horizontalLayout_5.addWidget(self.jntNb_label_2)
        self.cnxOffset_spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.cnxOffset_spinBox.setMinimum(0)
        self.cnxOffset_spinBox.setMaximum(9999)
        self.cnxOffset_spinBox.setProperty("value", 0)
        self.cnxOffset_spinBox.setObjectName("cnxOffset_spinBox")
        self.horizontalLayout_5.addWidget(self.cnxOffset_spinBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.jntNb_label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.jntNb_label_3.setObjectName("jntNb_label_3")
        self.horizontalLayout_6.addWidget(self.jntNb_label_3)
        self.bias_slider = QtWidgets.QSlider(self.groupBox_3)
        self.bias_slider.setMinimumSize(QtCore.QSize(0, 15))
        self.bias_slider.setMaximum(100)
        self.bias_slider.setProperty("value", 50)
        self.bias_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bias_slider.setObjectName("bias_slider")
        self.horizontalLayout_6.addWidget(self.bias_slider)
        self.bias_spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.bias_spinBox.setMaximum(100)
        self.bias_spinBox.setProperty("value", 50)
        self.bias_spinBox.setObjectName("bias_spinBox")
        self.horizontalLayout_6.addWidget(self.bias_spinBox)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.neutralPose_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.neutralPose_checkBox.setText("Neutral Pose")
        self.neutralPose_checkBox.setObjectName("neutralPose_checkBox")
        self.verticalLayout.addWidget(self.neutralPose_checkBox)
        self.onlyMaster_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.onlyMaster_checkBox.setText("Is Only Master (No Joints)")
        self.onlyMaster_checkBox.setObjectName("onlyMaster_checkBox")
        self.verticalLayout.addWidget(self.onlyMaster_checkBox)
        self.keepLength_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.keepLength_checkBox.setText("Keep Length")
        self.keepLength_checkBox.setObjectName("keepLength_checkBox")
        self.verticalLayout.addWidget(self.keepLength_checkBox)
        self.overrideNegate_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.overrideNegate_checkBox.setText("Override Negate Axis Direction For \"R\" Side")
        self.overrideNegate_checkBox.setObjectName("overrideNegate_checkBox")
        self.verticalLayout.addWidget(self.overrideNegate_checkBox)
        self.extraTweak_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.extraTweak_checkBox.setText("Extra Tweaks")
        self.extraTweak_checkBox.setObjectName("extraTweak_checkBox")
        self.verticalLayout.addWidget(self.extraTweak_checkBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.visHost_lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.visHost_lineEdit.setObjectName("visHost_lineEdit")
        self.horizontalLayout_3.addWidget(self.visHost_lineEdit)
        self.visHost_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.visHost_pushButton.setObjectName("visHost_pushButton")
        self.horizontalLayout_3.addWidget(self.visHost_pushButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.bias_spinBox, QtCore.SIGNAL("valueChanged(int)"), self.bias_slider.setValue)
        QtCore.QObject.connect(self.bias_slider, QtCore.SIGNAL("valueChanged(int)"), self.bias_spinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.groupBox_2.setTitle(gqt.fakeTranslate("Form", "Joint Options", None, -1))
        self.jntNb_label.setText(gqt.fakeTranslate("Form", "Joints Number", None, -1))
        self.groupBox_3.setTitle(gqt.fakeTranslate("Form", "Chain Master", None, -1))
        self.label_3.setText(gqt.fakeTranslate("Form", "Master B", None, -1))
        self.masterB_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))
        self.label.setText(gqt.fakeTranslate("Form", "Master A", None, -1))
        self.masterA_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))
        self.jntNb_label_2.setText(gqt.fakeTranslate("Form", "Connection Offset", None, -1))
        self.cnxOffset_spinBox.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>Index value to offset the connection between the Master chains and the slave chain. For example if the slave chain need to start the rotation from the second segment of the master chain, the offset will be 1.</p><p><span style=\" font-weight:600;\">WARNING</span>: If connection is out of index, will fallback to connect to the latest section in the master</p></body></html>", None, -1))
        self.jntNb_label_3.setText(gqt.fakeTranslate("Form", "Bias A/B", None, -1))
        self.groupBox_4.setTitle(gqt.fakeTranslate("Form", "Visibility UI host", None, -1))
        self.label_2.setText(gqt.fakeTranslate("Form", "Vis. Host", None, -1))
        self.visHost_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>In some situations the visibility channel controls  for FK and IK controls needs to be separated of the other component control channels.</p><p>If a host is set here will use this host as UI host for visibility channels. If nothing is set will use the regular UI host configuration.</p></body></html>", None, -1))
        self.visHost_pushButton.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>In some situations the visibility channel controls  for FK and IK controls needs to be separated of the other component control channels.</p><p>If a host is set here will use this host as UI host for visibility channels. If nothing is set will use the regular UI host configuration.</p></body></html>", None, -1))
        self.visHost_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))

