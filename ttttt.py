import numpy as np
class Reseau_Neurones:
    def __init__(self, nombre_couche, nombre_neurone_couche, valeur_init_poids, fonction_activation, nb_sortie):
        #definition des neurones avec poids
        #nombre_neurone_couche = liste de nb de couche elt
        self.nb_couche= nombre_couche
        self.nb_neurone_couche= nombre_neurone_couche
        self.f_activation=fonction_activation
        self.nb_sorties= nb_sortie

    def init_poids(self):
        for i in range(self.nb_couche):
            self.poids=np.random(0,1)

    def ouvrir_image(self,image):
        #divise l'image en pixel liste numpy de nuances de gris entre 0 et 255
        pass

    def forward(self,Poids,Valeurs):
        if Poids.shape[1] != Valeurs.shape[0]:
            print('erreur')
            return None
        NouvellesValeurs = np.dot(Poids, Valeurs)
        return self.sigmoid(NouvellesValeurs)
        # prend une matrice de nuances
        #return un nombre entre 0 et 1
        # si 5 neurones premieère couche ert 3 2e alors il y 6*3 poids 5+1 pour le biais
        #garder le resultat entre les différentes couches

        pass

    def backward(self,resultat):
        #mise à jour des poids

        pass

    def sigmoid(self,Valeurs):
        return 1 / (1 + np.exp(-Valeurs))
        # normalise les valeurs entre 0 et 1

matricemock= np.random(0,255, size=(60,60))
print(matricemock)

