# Apprentissage par renforcement

Un simple environnement pour explorer la mécanique de l'apprentissage par renforcement. Je reprendrai les notations notions de la page [wiki](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement)

# Modèle

## Overseer

Gérer les agents, apprentissage de la policy ?
## Agent
Policy: Une matrice de probabilité entre les états et les actions. C'est le "cerveau" d'un agent.

Trajectory: La suite S0, A0, R1, S1, A1, 
## Game
	- Un dictionnaire Etat/valeur
	- Des actions (de transition entre état) f(self, state, memory?) -> state
## Action
    f(self, state, memory?) -> state 
