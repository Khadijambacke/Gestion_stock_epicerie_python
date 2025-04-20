import json
from datetime import datetime
produit = {}

def charger_produits():
    global produit
    try:
        with open("produits.json", "r") as fichier:
            produit = json.load(fichier)
    except FileNotFoundError:
        produit = {}

def sauvegarder_produits():
    with open("produits.json", "w") as fichier:
        json.dump(produit, fichier, indent=4)

def nos(prix):
    if prix <= 0:
        raise ValueError("Le prix doit être strictement supérieur à 0")

def ajout():
    nom = input("Saisir le nom du produit : ").lower()
    if nom != "fin":
        try:
            prix = int(input("Saisir le prix du produit : "))
            nos(prix)
            stock = int(input("Saisir le stock du produit : "))
            vendus = int(input("Saisir le nombre de vente du produit : "))
            produit[nom] = {
                "prix": prix,
                "stock": stock,
                "vendus": vendus
            }
            sauvegarder_produits()
            print("Produit ajouté avec succès")
        except ValueError as e:
            print("Erreur :", e)

def misajour():
    n = input("Nom du produit à mettre à jour : ").lower()
    if n in produit:
        champ = input("Que voulez-vous modifier ? (prix/stock/vendus) : ").lower()
        try:
            nouvelle_valeur = int(input("Entrez la nouvelle valeur : "))
            if champ in produit[n]:
                produit[n][champ] = nouvelle_valeur
                sauvegarder_produits()
                print(f"{champ} mis à jour avec succès.")
            else:
                print("Champ invalide.")
        except ValueError:
            print("Valeur invalide.")
    else:
        print("Produit non trouvé.")
#enreistrement et historique
def charger_historique():
    global historique
    try:
        with open("historique.json", "r") as fichier:
            historique = json.load(fichier)
    except FileNotFoundError:
        historique = []
def sauvegarder_historique():
    with open("historique.json", "w") as fichier:
        json.dump(historique, fichier, indent=4)

def Enregistrer():
    nom = input("Saisir le nom du produit vendu : ").lower()
    if nom in produit:
        try:
            quantite = int(input("Combien de ventes avez-vous fait ? "))
            produit[nom]["vendus"] += quantite
            produit[nom]["stock"] -= quantite
            sauvegarder_produits()
            teda=datetime.now()
            prix = produit[nom]["prix"]
            date_vente = datetime.now().strftime("%Y-%m-%d")
            vente = {
                "produit": nom,
                "quantite": quantite,
                "prix": prix,
                "date": date_vente
            }

            charger_historique()
            historique.append(vente)
            sauvegarder_historique()

            print(f"Vente enregistrée a {teda}")
        except ValueError:
            print("Entrée invalide.")
    else:
        print("Produit non trouvé.")



def rupture(seuil):
    trouve = False
    for nom, info in produit.items():
        if info["stock"] <= seuil:
            print(f"{nom} (stock : {info['stock']})")
            trouve = True
    if not trouve:
        print("Aucun produit proche de la rupture.")

def vendus(minimum, maximum):
    trouve = False
    for nom, info in produit.items():
        if minimum <= info["vendus"] <= maximum:
            print(f"{nom} : {info}")
            trouve = True
    if not trouve:
        print("Aucun produit dans cette plage de ventes.")

def hausse():
    for nom in produit:
        produit[nom]["prix"] += produit[nom]["prix"] * hausse
    sauvegarder_produits()
    print(f"Hausse de{hausse} appliquée sur tous les prix.")
    for nom, info in produit.items():
        print(f"{nom} : {info}")
###



def vente_du_jour():
        try:
            # Charger l'historique
            with open("historique.json", "r") as fichier:
                historique = json.load(fichier)
        except FileNotFoundError:
            print("Aucune vente enregistrée pour le moment.")
            return

        date_du_jour = datetime.now().strftime("%Y-%m-%d")
        total = 0
        ventes_du_jour = []

        # Filtrer les ventes du jour
        for vente in historique:
            if vente["date"] == date_du_jour:
                ventes_du_jour.append(vente)
                total += vente["quantite"] * vente["prix"]

        if not ventes_du_jour:
            print(" Aucune vente pour aujourd'hui.")
            return

        # Affichage des ventes
        print(f"\nRapport des ventes pour le {date_du_jour} :\n")
        for vente in ventes_du_jour:
            nom = vente["produit"]
            quantite = vente["quantite"]
            prix = vente["prix"]
            sous_total = quantite * prix
            print(
                f"- {nom.capitalize()} | Quantité : {quantite} | Prix unitaire : {prix} FCFA | Total : {sous_total} FCFA")

        print(f"\n Montant total vendu aujourd'hui : {total} FCFA\n")






















