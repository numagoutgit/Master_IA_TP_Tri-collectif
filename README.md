# TP2_master_IA

**Résumé du sujet disponible sur SujeT_TP2_SMA.pdf :**

Il y a une grille MxN où sont disposés aléatoirement n_a objet de type A, n_b objet de type B et n_agent agents. Sur une même case il ne peut y avoir 2 agents ni deux objets. Les agents se déplace aléatoirement sur les huit directions disponibles et peuvent ramasser ou déposer un objet avec une probabilité dépendant de la proportion d'objets vus dans leur mémoire (voir le sujet pour plus de détail). Le but des agents est de trier la grille (cad réaranger les objets pour les regrouper).

**Implémentation :**

Pour implémenter ce problème j'ai crée plusieurs classes. 
- `Cell` : qui représente une case de la grille. Elle est caractérisée par ses coordonnées et si oui ou non un agent/objet est sur elle.
- `Objet` : qui représente les objets, ils sont caractérisés par leur type (A ou B)
- `Agent` : qui représente les agents. Ils sont caractérisés par la cellule où ils se situent, l'environnement où il se situe, 2 constantes permettant de calculer les probabilités de prise/dépot d'objet, une mémoire des dernieres cases parcourues et un taux d'erreur de discernement de l'objet. Les agents fonctionnent comme suit : 1) Il se déplace de manière aléatoire sur une des cases voisines libre. 2) S'il possède un objet et que la cellule n'a pas d'objet, il pose l'objet avec une probabilité. 3) S'il ne possède pas d'objet et que la case en possède un, il le ramasse avec un probabilité.
- `Environnement` : correspondant à l'environnement extérieur. Il est caractérisé par la grille. C'est cette classe qui possède la fonction principale `run` qui fait agir les agents. 

J'ai implémenté deux fonctions `run` pour prévoir deux manières de générer l'animation. 
- `run_without_saving` : qui après chaque tour des agents actualise le graphe, moins gourmant en mémoire et permet l'affichage du graphique avant la fin d'execution de tous les tous. Il ne permet cependant pas de sauvegarder la figure et les images par seconde sont limitées.
- `run_with_saving` : qui garde en mémoire toutes les positions de tous les agents et tous les objets à chaque tour, puis génère une animation avec. Gourmant en mémoire et prend du temps à ce lancer car il faut tout calculer avant de pouvoir afficher. La video est cependant sauvegardable et les images par secondes sont très bien.

**Executer :**

Télécharger le dossier, changer les paramètres du jeu et de l'animation dans `main.py`. Puis executer `python3 main.py` et suivre les instructions.
