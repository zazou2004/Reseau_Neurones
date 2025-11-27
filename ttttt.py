import numpy as np
class Reseau_Neurones:
    def __init__(self, nombre_couche, nombre_neurone_couche,  fonction_activation, nb_sortie,input):
        #definition des neurones avec poids
        #nombre_neurone_couche = liste de nb de couche elt
        self.nb_couche= nombre_couche
        self.nb_neurone_couche= nombre_neurone_couche
        self.f_activation= fonction_activation
        self.nb_sorties= nb_sortie
        self.PoidsetBiais = self.init_poids()
        self.Valeurs = [input]
    def init_poids(self):
        pass

    def ouvrir_image(self,image):
        #divise l'image en pixel liste numpy de nuances de gris entre 0 et 255
        pass

    def forward(self):
        for i in range(self.nb_couche):
            A = np.dot(self.PoidsetBiais[i],self.Valeurs[i])
            B = self.sigmoid(A)
            self.Valeurs.append(B)
        return self.Valeurs(self.nb_couche)


        pass

    def backward(self,resultat):
        #mise à jour des poids

        pass

    def sigmoid(self,Valeurs):
        return 1 / (1 + np.exp(-Valeurs))
        # normalise les valeurs entre 0 et 1

fausseimage= np.random(0,255, size=(60,60))
print(fausseimage)

