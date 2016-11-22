import sys
from PyQt4.QtGui import *
# Create an PyQT4 application object.
a = QApplication(sys.argv)
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()
 
# Set window size.
w.resize(320, 240)
 
# Set window title
w.setWindowTitle("Hello World!")
 
# adding a button 
btn = QPushButton('exit!', w)
btn.setToolTip('Click to quit!')
btn.clicked.connect(exit)
btn.resize(btn.sizeHint())
btn.move(100, 80)

# Create the actions
def on_click():
    print('clicked')
def on_press():
    print('pressed')
def on_release():
    print('released')
 
# connect the signals to the slots
btn = QPushButton('Click me', w)
btn.clicked.connect(on_click)
btn.pressed.connect(on_press)
btn.released.connect(on_release)

# Show window
w.show()
 
sys.exit(a.exec_())
