########################
# MITD-03
# Frédéric Li Combeau
# Lisa Vauvert
# Victor Combemorel
# Manel Mokrab
# https://github.com/uvsq-info/l1-python
########################

# Import des librairies

import tkinter as tk
import random as rd


########################

# Variables globales
global PROIES
global PREDATEURS

#########################

# Partie principale

root = tk.Tk()
root.title("Génération de terrain")

canvas = tk.Canvas(root, height=HAUTEUR, width=LARGEUR)
canvas.grid(column=1, row=0, rowspan=9)

# Création des widgets

bouton_init = tk.Button(text="Initialisation", command=init_terrain)
bouton_init.grid(column=0, row=0)

bouton_init = tk.Button(text="Play", command=play)
bouton_init.grid(column=0, row=1)

bouton_int = tk.Button(text="Interrompre", command=interruption)
bouton_int.grid(column=0, row=7)
bouton_rep = tk.Button(text="Reprendre", command=reprendre)
bouton_rep.grid(column=0, row=8)


init_affichage(init_terrain())
root.mainloop()

#Deplacement a copier/coller ensuite 
#p pour proie (pour l'instant à changer ensuite)
p = "proie" #juste pour pas casser les pieds bruh 


def deplacement():

    d=[]
    for i in range(8):
        i = 0
        d.append(i)

    r = rd.randit(1, 8)

    for i in range(len(d)):
        if i == 1:
            continue
        else:
            p.move(r)
            d.replace(r)
    

#Fonctions de Sauvegarde du coté proies et predateurs

fic_proies = open("sauvegarde_proies", "w")
fic_predateurs = open("sauvegarde_predateur", "w")

fic_proies.write (PROIES)
fic_predateurs.write (PREDATEURS)


fic_proies.close()
fic_predateurs.close()

fic_in = open("sauvegarde_proies", "r")
fic_out = open("sauvegarde_predateurs", "r")

fic_in.close()
fic_out.close()

def Sauvegarder():
    pass 

def Charger():
    pass

#donnees largeur et hauteur 
LARGEUR = 300
HAUTEUR = 300 #(à changer en fonction de ce qu'on mettra)
#Fonctions sauvegarde et charger tkinter

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)

sauvegarder = tk.Button(racine, text="Sauvegarder", command= Sauvegarder)
charger = tk.Button (racine, text="Charger", command= Charger)

#positionnement 
sauvegarder.grid(racine, row = 1, column = 1)
charger.grid(racine, row = 2, column = 1)
racine.mainloop()