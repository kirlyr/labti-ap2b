from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 300, 300)
    window.setWindowTitle("Data Diri")
    layout = QVBoxLayout()

    label_nama = QLabel("Nama")
    input_nama = QLineEdit()

    label_kelas = QLabel("Kelas")
    input_kelas = QLineEdit()

    button = QPushButton("Send")
    button.clicked.connect(lambda: on_clicked(input_nama.text(), input_kelas.text()))

    layout.addWidget(label_nama)
    layout.addWidget(input_nama)
    layout.addWidget(label_kelas)
    layout.addWidget(input_kelas)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    app.exec_()

def on_clicked(nama, kelas):
    message = QMessageBox()
    message.setText(f"Nama: {nama}\nKelas: {kelas}")
    message.exec_()

if __name__ == '__main__':
    main()
