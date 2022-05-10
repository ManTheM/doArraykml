# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_array2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(460, 397)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setMouseTracking(False)
        self.seismocode_pic = QtWidgets.QLabel(Form)
        self.seismocode_pic.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.seismocode_pic.setText("")
        self.seismocode_pic.setPixmap(QtGui.QPixmap("seismocode_icon.png"))
        self.seismocode_pic.setScaledContents(True)
        self.seismocode_pic.setObjectName("seismocode_pic")
        self.gb_utm = QtWidgets.QGroupBox(Form)
        self.gb_utm.setGeometry(QtCore.QRect(10, 220, 301, 141))
        self.gb_utm.setObjectName("gb_utm")
        self.formLayoutWidget = QtWidgets.QWidget(self.gb_utm)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 281, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.flout_utm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.flout_utm.setContentsMargins(0, 0, 0, 0)
        self.flout_utm.setObjectName("flout_utm")
        self.lbl_east = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_east.setObjectName("lbl_east")
        self.flout_utm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_east)
        self.lbl_north = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_north.setObjectName("lbl_north")
        self.flout_utm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_north)
        self.line_east = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_east.setObjectName("line_east")
        self.flout_utm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_east)
        self.line_north = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_north.setObjectName("line_north")
        self.flout_utm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_north)
        self.lbl_zone = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_zone.setObjectName("lbl_zone")
        self.flout_utm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_zone)
        self.lbl_hemi = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_hemi.setObjectName("lbl_hemi")
        self.flout_utm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_hemi)
        self.line_zone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_zone.setObjectName("line_zone")
        self.flout_utm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_zone)
        self.combob_eastnorth = QtWidgets.QComboBox(self.formLayoutWidget)
        self.combob_eastnorth.setObjectName("combob_eastnorth")
        self.combob_eastnorth.addItem("")
        self.combob_eastnorth.addItem("")
        self.flout_utm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.combob_eastnorth)
        self.Label_info = QtWidgets.QLabel(Form)
        self.Label_info.setGeometry(QtCore.QRect(80, 10, 351, 49))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Label_info.setFont(font)
        self.Label_info.setScaledContents(False)
        self.Label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_info.setWordWrap(True)
        self.Label_info.setObjectName("Label_info")
        self.gb_degree = QtWidgets.QGroupBox(Form)
        self.gb_degree.setGeometry(QtCore.QRect(10, 130, 231, 81))
        self.gb_degree.setObjectName("gb_degree")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.gb_degree)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 211, 51))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.flout_degree = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.flout_degree.setContentsMargins(0, 0, 0, 0)
        self.flout_degree.setObjectName("flout_degree")
        self.lbl_lon = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lbl_lon.setObjectName("lbl_lon")
        self.flout_degree.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_lon)
        self.lbl_lat = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lbl_lat.setObjectName("lbl_lat")
        self.flout_degree.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_lat)
        self.line_lat = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.line_lat.setObjectName("line_lat")
        self.flout_degree.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_lat)
        self.line_lon = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.line_lon.setObjectName("line_lon")
        self.flout_degree.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_lon)
        self.formLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 421, 51))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.flout_nameandtype = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.flout_nameandtype.setContentsMargins(0, 0, 0, 0)
        self.flout_nameandtype.setObjectName("flout_nameandtype")
        self.lbl_name = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.lbl_name.setObjectName("lbl_name")
        self.flout_nameandtype.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_name)
        self.line_name = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.line_name.setStatusTip("")
        self.line_name.setAutoFillBackground(False)
        self.line_name.setText("")
        self.line_name.setFrame(True)
        self.line_name.setClearButtonEnabled(True)
        self.line_name.setObjectName("line_name")
        self.flout_nameandtype.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_name)
        self.lbl_typeofcoordinate = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.lbl_typeofcoordinate.setObjectName("lbl_typeofcoordinate")
        self.flout_nameandtype.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_typeofcoordinate)
        self.combob_degreeORutm = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.combob_degreeORutm.setObjectName("combob_degreeORutm")
        self.combob_degreeORutm.addItem("")
        self.combob_degreeORutm.addItem("")
        self.flout_nameandtype.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combob_degreeORutm)
        self.gb_spec = QtWidgets.QGroupBox(Form)
        self.gb_spec.setGeometry(QtCore.QRect(250, 130, 181, 81))
        self.gb_spec.setObjectName("gb_spec")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.gb_spec)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 160, 51))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.flout_spec = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.flout_spec.setContentsMargins(0, 0, 0, 0)
        self.flout_spec.setObjectName("flout_spec")
        self.lbl_edge = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.lbl_edge.setObjectName("lbl_edge")
        self.flout_spec.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_edge)
        self.lbl_azim = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.lbl_azim.setObjectName("lbl_azim")
        self.flout_spec.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_azim)
        self.line_azi = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.line_azi.setObjectName("line_azi")
        self.flout_spec.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_azi)
        self.line_edge = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.line_edge.setObjectName("line_edge")
        self.flout_spec.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_edge)
        self.createkml = QtWidgets.QPushButton(Form)
        self.createkml.setGeometry(QtCore.QRect(330, 330, 81, 28))
        self.createkml.setObjectName("createkml")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CreateArray"))
        self.gb_utm.setTitle(_translate("Form", "UTM ( e.g. 295525.71 , 4409652.17 , 36 , N )"))
        self.lbl_east.setText(_translate("Form", "East"))
        self.lbl_north.setText(_translate("Form", "North"))
        self.lbl_zone.setText(_translate("Form", "Zone"))
        self.lbl_hemi.setText(_translate("Form", "Hemisphere"))
        self.combob_eastnorth.setItemText(0, _translate("Form", "North Hemisphere"))
        self.combob_eastnorth.setItemText(1, _translate("Form", "South Hemisphere"))
        self.Label_info.setText(_translate("Form", "Create Array Triangular Shape with coordinates using the Center point"))
        self.gb_degree.setTitle(_translate("Form", "Degree (e.g. 30.610951 , 39.812236 )"))
        self.lbl_lon.setText(_translate("Form", "Longitude"))
        self.lbl_lat.setText(_translate("Form", "Latitude"))
        self.lbl_name.setText(_translate("Form", "Name"))
        self.line_name.setWhatsThis(_translate("Form", "<html><head/><body><p>Give a name of kml file</p></body></html>"))
        self.lbl_typeofcoordinate.setText(_translate("Form", "Choose Type of Coordinate"))
        self.combob_degreeORutm.setItemText(0, _translate("Form", "Decimal Degree ( ° )"))
        self.combob_degreeORutm.setItemText(1, _translate("Form", "Universal Transverse Marcetor (UTM)"))
        self.gb_spec.setTitle(_translate("Form", "Specifications ( e.g. 500 , 20 )"))
        self.lbl_edge.setText(_translate("Form", "Edge (m)"))
        self.lbl_azim.setText(_translate("Form", "Azimuth ( ° )"))
        self.line_azi.setText(_translate("Form", "0"))
        self.createkml.setText(_translate("Form", "Create kml"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
