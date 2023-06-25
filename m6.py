from PyQt5.QtWidgets import *

def main():
    app = QApplication ([])
    window = QWidget ()
    window. setGeometry (200, 200, 400, 600) 
    window.setWindowTitle("m. irfan tri atsal / 51422080 - 1IA04")
    layout = QVBoxLayout ()
    label = QLabel("Pesan Singkat Buat Asisten dan PJ")
    button = QPushButton ("Buka!")
    button.clicked.connect (on_clicked)
    layout. addWidget (label)
    layout. addWidget (button)
    window.setLayout (layout)
    window.show()
    app.exec_()
def on_clicked():
    message = QMessageBox()
    message. setText ("Kocak")
    message.exec_()

if __name__ == '__main__':
    main()