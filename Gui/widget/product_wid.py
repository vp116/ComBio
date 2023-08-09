from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpinBox, QFrame


class ProductWidget(QWidget):
    def __init__(self, nom="Grain de mais", des="ce sont des graines qui changent", prix="155$"):
        super().__init__()
        self.setFixedSize(600, 200)

        # Style du widget lui-même
        self.setStyleSheet('''
            ProductWidget {
                background-color: #f8f9fa;
                border: 1px solid #ced4da;
                border-radius: 5px;
                padding: 10px;
            }
        ''')

        # Style des boutons
        button_style = '''
            QPushButton {
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        '''

        # Style du SpinBox
        spinbox_style = '''
            QSpinBox {
                border: 1px solid #ced4da;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                subcontrol-origin: border;
                subcontrol-position: top right;
                width: 0px;
            }
        '''

        self.bouton_add = QPushButton("+")
        self.bouton_add.setFixedSize(35, 35)
        self.bouton_add.setStyleSheet(button_style)

        self.bouton_rem = QPushButton("-")
        self.bouton_rem.setFixedSize(35, 35)
        self.bouton_rem.setStyleSheet(button_style)

        self.bouton_delete = QPushButton()
        self.bouton_delete.setFixedSize(40, 40)
        self.bouton_delete.setStyleSheet('''
            QPushButton {
                border: none;
                background-color:#ccc;
                /*border-image: url(delete.png);
            }
        ''')

        self.bouton_im_prod = QPushButton()
        self.bouton_im_prod.setFixedSize(101, 101)

        self.quantite = QSpinBox()
        self.quantite.setFixedSize(50, 35)
        self.quantite.setStyleSheet(spinbox_style)

        self.label_prix = QLabel(prix)
        self.label_prix.setStyleSheet('''
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
        ''')

        self.label_desc = QLabel(des)
        self.label_desc.setStyleSheet('''
            QLabel {
                font-size: 14px;
            }
        ''')

        self.label_name = QLabel(nom)
        self.label_name.setStyleSheet('''
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
        ''')

        layout = QVBoxLayout()
        layout_add = QHBoxLayout()
        layout_quantite = QHBoxLayout()
        layout_quantite.addWidget(self.bouton_rem)
        layout_quantite.addWidget(self.quantite)
        layout_quantite.addWidget(self.bouton_add)

        layout_label = QVBoxLayout()
        layout_label.addWidget(self.label_name)
        layout_label.addWidget(self.label_desc)
        layout_label.addWidget(self.label_prix)

        frame_info_prod = QFrame()
        frame_info_prod.setLayout(layout_label)

        bottom_frame = QFrame()
        bottom_frame.setLayout(layout_quantite)

        nex_frame = QFrame()

        layout_add.addWidget(self.bouton_im_prod)
        layout_add.addWidget(frame_info_prod)
        layout_add.addWidget(self.bouton_delete, alignment=Qt.AlignTop | Qt.AlignRight)
        nex_frame.setLayout(layout_add)

        layout.addWidget(nex_frame)
        layout.addWidget(bottom_frame, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.bouton_add.clicked.connect(lambda: self.move_quantite(1))
        self.bouton_rem.clicked.connect(lambda: self.move_quantite(-1))

    def move_quantite(self, step):
        qte = self.quantite.value()
        qte += step
        # Vérifier que la quantité ne devient pas négative ou nulle
        qte = max(0, qte)
        self.quantite.setValue(qte)


if __name__ == "__main__":
    app = QApplication([])
    win = ProductWidget()
    win.show()
    app.exec()
