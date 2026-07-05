import sqlite3
from datetime import datetime

# Connexion à la base de données
conn = sqlite3.connect('menuiserie_db.sqlite')
cursor = conn.cursor()

import tkinter as tk

# Fonction pour ajouter une tâche
def connecter_bd():
    return sqlite3.connect('menuiserie_db.sqlite')
def ajouter_tache(pr_cle, description):
    cursor.execute('''
    INSERT INTO Table_Code_Tache (Pr_cle, Description)
    VALUES (?, ?)
    ''', (pr_cle, description))
    conn.commit()
    return cursor.lastrowid

# Fonction pour ajouter une attribution
def ajouter_attribution(cle, description, lien_variante):
    cursor.execute('''
    INSERT INTO Table_Attribution (Ta_Attribution_cle, Ta_Attribution_Description, Ta_Attribution_Lien_Variante)
    VALUES (?, ?, ?)
    ''', (cle, description, lien_variante))
    conn.commit()
    return cursor.lastrowid

# Fonction pour ajouter une variante
def ajouter_variante(at_cl, at_description):
    cursor.execute('''
    INSERT INTO Table_Variante (At_cl, At_Desciption)
    VALUES (?, ?)
    ''', (at_cl, at_description))
    conn.commit()
    return cursor.lastrowid

# Fonction pour lier une tâche à une variante
def lier_tache_variante(ltv_cle, ltv_lien_tache, lien_attribution):
    cursor.execute('''
    INSERT INTO Table_Lien_Tache_Variante (LTV_cle, LTV_Lien_Tache, Lien_Attribution)
    VALUES (?, ?, ?)
    ''', (ltv_cle, ltv_lien_tache, lien_attribution))
    conn.commit()
    return cursor.lastrowid

# Fonction pour ajouter ou mettre à jour les taux horaires et profits
def maj_taux_horaire_profit(code, description, taux_horaire, profit_total, profit_mat, profit_md):
    cursor.execute('''
    INSERT OR REPLACE INTO Table_tauxHoraire_profit 
    (CP_Code, CP_Descrip, CP_Taux_Horaire, CP_Pour_Profit_total, CP_Pour_Profit_Mat, CP_Pour_Profit_MD)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (code, description, taux_horaire, profit_total, profit_mat, profit_md))
    conn.commit()
    return cursor.lastrowid

# Fonction pour ajouter une entrée dans TableOrigine
def ajouter_travail(nom_travail, conv_par_marche, teinture_temps, teinture_cout, vernis_temps, vernis_cout,
                    fabrication_cout, installation_temps, installation_cout, main_oeuvre_temps, 
                    main_oeuvre_cout, materiel_cout, unit_mes):
    cursor.execute('''
    INSERT INTO TableOrigine (Nom travau, Conv par marche, Teinture Temps, Teinture Cout, 
    Vernis Temps, Vernis  Cout, Fabrication Cout, Installation Temps, Installation Cout, 
    Main d'oeuv Temps, Main D'oeuv Cout, Materiel Cout, Unit Mes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nom_travail, conv_par_marche, teinture_temps, teinture_cout, vernis_temps, vernis_cout,
          fabrication_cout, installation_temps, installation_cout, main_oeuvre_temps, 
          main_oeuvre_cout, materiel_cout, unit_mes))
    conn.commit()
    return cursor.lastrowid
def afficher_taches():
    conn = connecter_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT Pr_cle, Description FROM Table_Code_Tache")
    taches = cursor.fetchall()
    conn.close()
    
    fenetre_taches = tk.Toplevel(fenetre)
    fenetre_taches.title("Liste des tâches")
    
    for tache in taches:
        tk.Label(fenetre_taches, text=f"{tache[0]} - {tache[1]}").pack()

def afficher_attributions():
    conn = connecter_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT Ta_Attribution_cle, Ta_Attribution_Description FROM Table_Attribution")
    attributions = cursor.fetchall()
    conn.close()
    
    fenetre_attributions = tk.Toplevel(fenetre)
    fenetre_attributions.title("Liste des attributions")
    
    for attribution in attributions:
        tk.Label(fenetre_attributions, text=f"{attribution[0]} - {attribution[1]}").pack()

def afficher_variantes():
    conn = connecter_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT At_cl, At_Desciption FROM Table_Variante")
    variantes = cursor.fetchall()
    conn.close()
    
    fenetre_variantes = tk.Toplevel(fenetre)
    fenetre_variantes.title("Liste des variantes")
    
    for variante in variantes:
        tk.Label(fenetre_variantes, text=f"{variante[0]} - {variante[1]}").pack()

# Ajout des boutons pour afficher les listes
fenetre = tk.Tk()
fenetre.title("Gestion de la menuiserie")

btn_afficher_taches = tk.Button(fenetre, text="Afficher les tâches", command=afficher_taches)
btn_afficher_taches.pack(pady=10)

btn_afficher_attributions = tk.Button(fenetre, text="Afficher les attributions", command=afficher_attributions)
btn_afficher_attributions.pack(pady=10)

btn_afficher_variantes = tk.Button(fenetre, text="Afficher les variantes", command=afficher_variantes)
btn_afficher_variantes.pack(pady=10)

# Lancement de l'application
fenetre.mainloop()

# N'oubliez pas de fermer la connexion à la base de données quand vous avez terminé
# conn.close()
