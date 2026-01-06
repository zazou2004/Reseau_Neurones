import numpy as np
class Reseau_Neurones:
    def __init__(self, nombre_couche, nombre_neurone_couche,  fonction_activation, nb_sortie,input, h_image, l_image):
        #definition des neurones avec poids
        #nombre_neurone_couche = liste de nb de couche elt
        self.nb_couche= nombre_couche
        self.nb_neurone_couche= nombre_neurone_couche
        self.f_activation= fonction_activation #ça c'est la sigmoid sert à rien ici ?
        self.nb_sorties= nb_sortie

        self.n = 1 + h_image * l_image #taille du vecteur
        self.h_image = h_image
        self.l_image = l_image
        self.w=np.zero(self.n) #poids
        self.Valeurs = [np.zeros(self.n)]
    def init_poids(self):
        pass

    def ouvrir_image(self,image):
        #divise l'image en pixel liste numpy de nuances de gris entre 0 et 255
        """
        Découpe l'image en w x h cases et calcule la proportion de pixels noirs
        L'image_pixels est supposée être déjà recadrée (bounding box).
        """
        # (Logique simplifiée de découpage en grille)
        # On calcule les proportions pour chaque case [cite: 30]
        proportions = []
        # ... calcul des proportions ...

        # On ajoute la valeur constante 1 à la fin (n-ième composante) [cite: 13, 31]
        vecteur_x = np.array(proportions + [1.0])
        return vecteur_x

    def forward(self, x):
        self.Valeurs[0]=x

        # sans la fonction sigmoïd
        A = np.dot(self.w,self.Valeurs[0])

        if A>0:
            return 1
        else:
            return 0


    def backward(self,resultat):
        #mise à jour des poids
        for j in self.nb_sorties:
            errors = resultat[j] - self.Valeurs[j]
        for l in range (-(self.nb_couche+1), 1):
            for i in range(self.nb_neurone_couche):



            pass

    def sigmoid(self,Valeurs):
        return 1 / (1 + np.exp(-Valeurs))
        # normalise les valeurs entre 0 et 1

fausseimage= np.random(0,255, size=(60,60))
print(fausseimage)

#valeur[0]: image