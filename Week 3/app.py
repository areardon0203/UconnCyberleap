from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.setGeometry(10,10,500,200)
window.move(290,15)

helloWorld = QLabel("Hello World", parent=window)
helloWorld.setFont(QFont('Arial Font', 80))
helloWorld.move(60,15)
window.show()  # IMPORTANT!!!!! Windows are hidden by default.
# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
