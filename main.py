import numpy as np
class Reseau_Neurones:
    def __init__(self,taille_entree, nombre_couche, nombre_neurone_couche, valeur_init_poids, fonction_activation, nb_sortie):
        #definition des neurones avec poids
        #nombre_neurone_couche = liste de nb de couche elt
        self.nb_neurone_couche = [taille_entree] + nombre_neurone_couche + nb_sortie # la première couche dépend de la taille de l'image, la dernière ici 1 ou 0 donc 1
        self.nb_couche= nombre_couche
        self.f_activation=fonction_activation
        self.nb_sorties= nb_sortie
        self.poids=[]
        self.biais=[]

        self.init_poids()

    def init_poids(self):
        for i in range(self.nb_couche):
            taille_entree_couche = self.tailles_couches[i]
            taille_sortie_couche = self.tailles_couches[i + 1]
            W= np.random.uniform(low=0.0, high=1.0, size=(taille_entree_couche,taille_sortie_couche))
            self.poids.append(W)


    def ouvrir_image(self,image):
        #divise l'image en pixel liste numpy de nuances de gris entre 0 et 255
        pass

    def forward(self,mat):
        # prend une matrice de nuances
        #return un nombre entre 0 et 1
        # si 5 neurones premieère couche ert 3 2e alors il y 6*3 poids 5+1 pour le biais
        #garder le resultat entre les différentes couches

        pass

    def backward(self,resultat):
        #mise à jour des poids
        pass

matricemock= np.random(0,255, size=(60,60))
print(matricemock)

