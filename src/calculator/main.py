#!/usr/bin/env python3

#Autor: Ondřej Andrla
import sys
import calc_lib as calc
from PyQt5.QtWidgets import QApplication
import QtQml
#from calculator import CalculatorWindow, Convertor
from PySide import QtCore, QtGui, QtDeclarative


def on_qml_mouse_clicked():
    MyClickButton.clicked.connect(on_qml_mouse_clicked)
class Backend(QObject):
    calc = Signal(str)

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.m_text = ""

    @Property(str, notify=textChanged)
    def text(self):
        return self.m_text

    @text.setter
    def setText(self, text):
        if self.m_text == text:
            return
        self.m_text = text
        self.textChanged.emit(self.m_text)
        class Foo(QObject):
            def __init__(self, *args, **kwags):
                QObject.__init__(self, *args, **kwags)
                self._progress = 0
                def sub(self):
                    substitution = component.create()
                def div(self):
                    division = component.create()
                def add(self):
                    addition = component.create()
                def mull(self):
                    multiplication = component.create()
            @pyqtSlot()
            def calc_lib(self):
                self.runnable = Runnable(self)
                QThreadPool.globalInstance().start(self.runnable)

            progressChanged = pyqtSignal(int)

            @pyqtProperty(int, notify=progressChanged)
            def progress(self):
             qmlRegisterType(add, 'add', 1, 0, 'add')
             qmlRegisterType(sub, 'sub', 1, 0, 'sub')
             qmlRegisterType(mull, 'mull', 1, 0, 'mull')
             qmlRegisterType(div, 'div', 1, 0, 'div')
             qmlRegisterType(fac, 'fac', 1, 0, 'fac')
             qmlRegisterType(log, 'log', 1, 0, 'log')
             qmlRegisterType(pow, 'pow', 1, 0, 'pow')
             qmlRegisterType(root, 'root', 1, 0, 'root')
                return self._progress


            @pyqtSlot(QVariant, QVariant, QVariant)
            def funct1(self, val1, val2, myengine):

                result = val1*val2

                obj = myengine.rootObjects()
                myObject = obj[0].findChild(QObject, 'myGui')
                QMetaObject.invokeMethod(myObject, "myTest1", Qt.DirectConnection,
        Q_ARG(int,result))

            @pyqtSlot(int)
            def updateProgress(self, value):
                if self._progress == value:
                    return
                self._progress = value
                self.progressChanged.emit(self._progress)

            def count(self):
                for i in range(100):
                    QMetaObject.invokeMethod(self, "updateProgress",
                                             Qt.QueuedConnection,
                                             Q_ARG(int, i))
                    QThread.msleep(1000)



app = QtGui.QGuiApplication([])


calculator = CalculatorWindow()


sys.exit(app.exec_())
