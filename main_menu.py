import application

def safar():
    application.charger_produits()
    while True:
        print("\n==== MENU ====")
        print("1. Ajouter un produit")
        print("2. Mettre à jour le stock")
        print("3. Enregistrer une vente")
        print("4. Voir les produits les plus vendus")
        print("5. Voir les produits presque en rupture")
        print("6. Appliquer une hausse de 10% sur tous les prix")
        print("0. Quitter")
        try:
            choix = int(input("Faites votre choix : "))
            match choix:
                case 1:
                    application.ajout()
                case 2:
                    application.misajour()
                case 3:
                    application.Enregistrer()
                case 4:
                    min_vente = int(input("Définir le minimum de vente : "))
                    max_vente = int(input("Définir le maximum de vente : "))
                    application.vendus(min_vente, max_vente)
                case 5:
                    seuil = int(input("Saisir le seuil de rupture : "))
                    application.rupture(seuil)
                case 6:
                    application.hausse()
                case 0:
                    print("Merci d'avoir utilisé le programme.")
                    break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    safar()




