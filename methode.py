from qt_core import *


def setup_user_info_layout(self):
    # Création du layout pour les informations des utilisateurs
    layout_utilisateurs = QVBoxLayout()
    layout_utilisateurs.setContentsMargins(7, 0, 7, 0)

    # Récupération des clients dans la base de données en utilisant la classe de gestion de la BDD
    query = "SELECT * FROM clients"
    list_clients = self.gestionnaire_db.executer_requete_fetchall(query)

    # Ajout des utilisateurs
    for client in list_clients:
        utilisateur = table_info(nom=client[1], email=client[2], numero=client[4])
        layout_utilisateurs.addWidget(utilisateur)

        # Récupération des boutons "Modifier" et "Supprimer" de chaque utilisateur
        bouton_supprimer = utilisateur.get_bouton_supprimer()

        # Connexion des signaux des boutons aux slots correspondants
        bouton_supprimer.clicked.connect(self.on_supprimer_clicked)

    # Ajout du layout des utilisateurs à la zone de défilement
    self.pages.scroll_area_content.setLayout(layout_utilisateurs)


def display_tab(self):
    # Récupération des produits dans la base de données en utilisant la classe de gestion de la BDD
    query = "SELECT * FROM produits"
    list_produits = self.gestionnaire_db.executer_requete_fetchall(query)

    result = [(produit[1], produit[4]) for produit in list_produits]  # Création de la liste des tuples (nom, qte)

    self.pages.stock_tab.setRowCount(0)

    for row_number, row_data in enumerate(result):
        self.pages.stock_tab.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            item = QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)  # Centrer le texte
            self.pages.stock_tab.setItem(row_number, column_number, item)


def display_prod(self):
    # Récupération des produits dans la base de données en utilisant la classe de gestion de la BDD
    query = "SELECT * FROM produits"
    list_produits = self.gestionnaire_db.executer_requete_fetchall(query)

    result1 = [produit[1] for produit in list_produits]  # Création de la liste des noms de produits

    # Nettoyer et mettre à jour la combobox avec les noms des produits
    self.pages.liste_prod_combo_box.clear()
    self.pages.liste_prod_combo_box.addItems(result1)


def ajouter_Produit(self):
    nom_prod = self.pages.nom_prod_le.text()
    categorie_prod = self.pages.categorie_prod_le.text()
    prix_prod = self.pages.prix_prod_le.text()
    qte = self.pages.textEdit.toPlainText()

    # Utilisation de votre classe de gestion de la base de données pour exécuter la requête
    insert_query = "INSERT INTO produits (libelle, prixvente, codecateg, qte) VALUES (%s, %s, %s, %s);"
    valeurs = (nom_prod, prix_prod, categorie_prod, qte)
    if self.gestionnaire_db.executer_requete(insert_query, valeurs):
        print("Produit ajouté avec succès.")


def supprimer_Produit(self):
    nom_prod = self.pages.liste_prod_combo_box.currentText()
    delete_query = "DELETE FROM produits WHERE libelle=%s;"
    if self.gestionnaire_db.executer_requete(delete_query, (nom_prod,)):
        print("Produit supprimé avec succès.")

# Autres méthodes de la classe...
