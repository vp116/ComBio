import os
import sys

from manage_data import ManageData
from methode import toggleMenu
from qt_core import *
from ui_main_app import Ui_MainWindow

os.environ["QT_FONT_DPI"] = "96"


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # # Créez une instance de votre classe de gestion de la base de données
        # self.gestionnaire_db = ManageData(
        #     host="localhost",
        #     user="root",
        #     password="",
        #     database="projetgl"
        # )

        self.ui.toogle_menu.clicked.connect(lambda: toggleMenu(self, 245))

    # def closeEvent(self, event):
    #
    #     réponse = QMessageBox(self)
    #     réponse.setWindowTitle("Message")
    #     réponse.setText("Êtes-vous sûr de vouloir quitter ?")
    #     réponse.setIcon(QMessageBox.Question)
    #     réponse.setStyleSheet("""
    #              QMessageBox {
    #                  background-color: #f8f8f8;
    #                  border: 2px solid #c3c3c3;
    #                  border-radius: 5px;
    #                  font-size: 14px;
    #                  padding: 10px;
    #              }
    #
    #              QMessageBox QLabel {
    #                  color: #000000;
    #                  font-weight: bold;
    #              }
    #
    #              QMessageBox QPushButton {
    #                  background-color: #f0f0f0;
    #                  border: 2px solid #c3c3c3;
    #                  border-radius: 5px;
    #                  font-size: 12px;
    #                  padding: 5px;
    #                  min-width: 80px;
    #              }
    #
    #              QMessageBox QPushButton:hover {
    #                  background-color: #d0d0d0;
    #              }
    #          """)
    #
    #     # Ajouter une icône personnalisée
    #     # icone = QIcon("images/image/btp.ico")
    #     # réponse.setWindowIcon(icone)
    #
    #     réponse.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    #     réponse.button(QMessageBox.Yes).setText("Oui")
    #     réponse.button(QMessageBox.No).setText("Non")
    #     réponse.setDefaultButton(QMessageBox.No)
    #
    #     if réponse.exec() == QMessageBox.Yes:
    #         event.accept()
    #     # elif not self.confirm_deconnexion:
    #     #     event.ignore()
    #
    #     else:
    #         event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())
