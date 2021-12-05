# TP2_master_IA Version 2

**Résumé du sujet disponible sur SujeT_TP2_SMA.pdf :**

Il y a une grille MxN où sont disposés aléatoirement n_a objet de type A, n_b objet de type B, n_C objet de type C et n_agent agents. Sur une même case il ne peut y avoir 2 agents ni deux objets. Les agents se déplace aléatoirement sur les huit directions disponibles et peuvent ramasser ou déposer un objet avec une probabilité dépendant de la proportion d'objets vus dans leur mémoire (voir le sujet pour plus de détail). Le but des agents est de trier la grille (cad réaranger les objets pour les regrouper).

Cette version diffère de la version 1 par l'ajout d'une troisième catégorie d'objet, les objets C. Ceux-ci sont trop lourd et un agent a besoin de l'aide d'un autre agent pour le déplacer.

**Implémentation**

J'utilise la même implémentation que la version 1 mais avec quelques ajouts sur les classes :
- `Cell` : possède un nouvel attribut `taux` représentant sont taux de phéromone. Cet attribut requiert des nouvelles méthodes, une méthode de dissipation de la phéromone avec un taux `r` et les setters/getters habituels.
- `Agent` : Les agents possèdent maintenant un état dans lequel ils sont et qui modifie leur comportement (follow, leader, free, help et Looking for). Ces états représentent chacun un état par lequel ils passent lors de la coopération.
  - `help` : L'agent dans cet état reste immobile sur un objet C et diffuse de la phéromone sur les cases voisines.
  - `follow` : L'agent suit son leader et attend que celui-ci pose son objet.
  - `Looking for` : L'agent cherche l'emetteur de phéromone en se déplaçant vers les cellules possédant un taux de phéromone plus élevé. Si il se trouve déjà sur le maximum alors il balcule en `free` (cela veut dire qu'un autre agent à déjà aidé celui qui émettait), si il trouve celui qui émettait alors il balcule en `follow` et l'émetteur balcule en `leader`.
  - `free` : Les agents fonctionnent comme dans la version 1 (mouvement aléatoire et probabilité de prise/dépot). Cependant s'il tombe sur un objet C et qu'il souhaite le ramasser il balcule dans l'état `help`. De plus s'il sent de la phéromone à un taux assez élevé il balcule dans l'état `Looking for`.
   - `leader` : L'agent se comporte comme en `free` mais il porte un objet C, un agent le suit (l'aide) et s'il souhaite déposer un objet alors il le dépose et le suiveur ainsi que lui-même bascule en `free`.

Dans le code, les agents ont donc deux attributs supplémentaire, `leader` et `follower` qui représente respectivement le leader (si l'agent est un follower) et le follower (si l'agent est un leader).

**Gif d'animation**

![](image_rapport/animation_v2.gif?raw=true)

Si on regarde bien on voit bien que des agents se pose sur les objets vert, puis qu'un autre agent se colle à eux. Enfin l'objet vers est ramassé puis les deux agents se suivent jusqu'à ce que le leader dépose l'objet.

