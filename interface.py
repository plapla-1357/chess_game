from PySide6 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        
        
app = QtWidgets.QApplication([])
window = Window()
window.show()
app.exec()