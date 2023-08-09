import os

from manage_data import ManageData
from qt_core import *

os.environ["QT_FONT_DPI"] = "96"


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Créez une instance de votre classe de gestion de la base de données
        self.gestionnaire_db = ManageData(
            host="localhost",
            user="root",
            password="",
            database="projetgl"
        )


if __name__ == '__main__':
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec()
