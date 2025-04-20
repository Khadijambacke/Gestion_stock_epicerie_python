import json

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

def Enregistrer():
    nom = input("Saisir le nom du produit vendu : ").lower()
    if nom in produit:
        try:
            quantite = int(input("Combien de ventes avez-vous fait ? "))
            produit[nom]["vendus"] += quantite
            produit[nom]["stock"] -= quantite
            sauvegarder_produits()
            print("Vente enregistrée.")
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














git






