## Table des matières
* [Informations générales](#informations-générales)
* [Technologies utilisées](#technologies-utilisées)
* [Caractéristiques](#caractéristiques)
* [Installation](#installation)
* [Information](#information)
* [L'état du projet](#l-'-état-du-projet)
* [Auteurs](#auteurs)


## Informations générales

Projet 10 formation Open Classrooms : Créez une API sécurisée RESTful en utilisant Django REST.

## Technologies utilisées

Python - version 3.9.5

Django - version 4.1

Postman

## Caractéristiques

Développer une application de emonter et de suivi de problème techniques via la mise en place d’une API REST à l'aide du framework REST Django.

## Installation 

Vous devez installer l'application "SoftDesk" disponible sur le lien : 
https://github.com/Formation-DA-PYTHON2021/P10.git

#### Récupération du projet : 

Copie dans un répértoire les éléments:

``git clone https://github.com/Formation-DA-PYTHON2021/P10.git``

#### Activer l'environnement virtuel : 

``cd P10``

``python -m venv env``

``source env\Scripts\activate``

#### Installer les paquets requis avec la commande : 

``pip install -r requirements.txt``

#### Démarage : 

- Lancer le serveur Django avec la commande : 

``python manage.py runserver``

- Dans le navigateur de votre choix, se rendre à l'adresse http://127.0.0.1:8000/

## Information 
#### Fonctionnalités :
- S'inscrire, se connecter et se déconnecter  ;
- Consulter, créer, modifier, supprimer un projet selon ses autorisations;
- Ajouter, consulter, modifier, supprimer un contributeur selon ses autorisations;
- Consulter, créer, modifier, supprimer un problème selon ses autorisations;
- Consulter, créer, modifier, supprimer un commentaire selon ses autorisations.

L'utilisateur ne peut avoir accès à ces fonctionnalités que si il a les permissions necessaire.

#### Permissions : 
- L'accès est autorisé si l'utilisateur est connecté.
- L'utilisateur connecté est autorisé à créer un projet.
- L'auteur d'un projet, problème ou commentaire, est autorisé à modifier ou supprimer un élément comme projet, contributeur, problème, commentaires. nb: un auteur est un contributeur spécifique.
- Le contributeur est autorisé à consulter, créer les éléments suivant : projet, contributeur, problème, commentaire.

#### Liste des utilisateurs existants :

| Nom           | Mot de Passe  |
| ------------- | ------------- |
| Superuser     | S3cret!!      |
| Contrib1      | S3cret!!      |
| Contrib2      | S3cret!!      |

#### Point de terminaison : 

| |Point de  terminaison d'API|Méthode HTTP|URL|
|--| ---------------------------- | ------------- | ------------- |
|1|Inscription de l'utilisateur|POST|/signup/|
|2|Connexion de l'utilisateur|POST|/login/|
|3| Déconnexion|POST|/logout/|
|4|Récupérer la liste de tous les projects rattachés à l'utilisateur connecté|GET|/projects/|
|5|Créer un projet|POST|/projects/|
|6|Récupérer les détails d'un project via son id|GET|/projects/{id}/|
|7|Mettre à jour un projet|PUT|/projects/{id}/|
|8|Supprimer un projet et ses problèmes|DELETE|/projects/{id}/|
|9|Ajouter un utilisateur (collaborateur) attachés à un projet |POST|/projects/{id}/users/|
|10|Récupérer la liste de tous les utilisateur (users) attachés à un projet| GET|/projects/{id}/users/|
|11|Supprimer un utilisateur d'un projet|DELETE|/projects/{id}/users/{id}/|
|12|Récupérer la liste des problèmes liès à un projet|GET|/projects/{id}/issues/|
|13|Créer un problème dans un projet|POST|/projects/{id}/issues/|
|14|Mettre à jour un problème dans un projet|PUT|/projects/{id}/issues/{id}/|
|15|Supprimer un problème dans un projet|DELETE| /projects/{id}/issues/{id}/|
|16|Créer des commentaires sur un problème dans un projet|POST |/projects/{id}/issues/{id}/comments/{id}/|
|17|Récupérer la liste de tout les commentaires liès à un problème|GET| /projects/{id}/issues/{id}/comments/|
|18|Mettre à jour un commentaire|PUT|/projects/{id}/issues/{id}/comments/{id}/|
|19|Suppprimer un commentaire|DELETE|/projects/{id}/issues/{id}/comments/{id}/  |
|20|Récupérer un commentaire via son id|GET|/projects/{id}/issues/{id}/comments/{id}/|


#### Documentation
La documentation Postman du projet est disponible sur le lien :

``https://documenter.getpostman.com/view/23674249/2s8YRjoYDH``


## L'état du projet

Le projet est : complet



## Auteurs

T. CALVET
